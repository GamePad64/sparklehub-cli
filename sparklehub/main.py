#! /usr/bin/env python3
import copy
import sys
import tempfile
import uuid
from typing import BinaryIO, Dict, Optional, Union

import click
import httpx
from colorama import Fore
from colorama import init as colorama_init
from sparklehub import openapi_client
from sparklehub.consts import SignatureType
from sparklehub.helpers import signature
from tqdm import tqdm

configuration = openapi_client.Configuration(
    host=f"https://api.sparklehub.io/v1/sparkle",
    api_key={"Authorization": ""},
    api_key_prefix={"Authorization": "Token"},
)


def sign_file(f: BinaryIO, dsa_privkey: Optional[bytes] = None, eddsa_privkey: Optional[str] = None):
    signatures: Dict[SignatureType, str] = {}

    if dsa_privkey is not None:
        signatures[SignatureType.DSA] = signature.sign_dsa_b64(f, private_key=dsa_privkey)
        print(Fore.GREEN + f"Generated DSA signature: {signatures[SignatureType.DSA]}", file=sys.stderr)

    if eddsa_privkey is not None:
        signatures[SignatureType.EdDSA] = signature.sign_ed25519_b64(f, private_key=eddsa_privkey)
        print(Fore.GREEN + f"Generated EdDSA signature: {signatures[SignatureType.EdDSA]}", file=sys.stderr)

    return signatures


def sign_remote_file(url: str, **signer_kwargs):
    with tempfile.SpooledTemporaryFile(10 * 1024 * 1024) as f:
        with httpx.stream("GET", url) as r:
            pbar = tqdm(total=int(r.headers["content-length"]), unit="B", unit_scale=True, desc=str(r.url))
            for data in r.iter_bytes():
                f.write(data)
                pbar.update(len(data))
            pbar.close()

        return sign_file(f, **signer_kwargs)


def read_keys(
    dsa_privkey_f: Optional[BinaryIO] = None,
    eddsa_privkey: Optional[str] = None,
    eddsa_privkey_f: Optional[BinaryIO] = None,
    eddsa_privkey_keychain: bool = False,
) -> Dict[str, Union[str, bytes]]:
    signer_kwargs: Dict[str, Union[str, bytes]] = {}

    if dsa_privkey_f is not None:
        dsa_privkey_f.seek(0)
        signer_kwargs["dsa_privkey"] = dsa_privkey_f.read()

    if eddsa_privkey is not None:
        signer_kwargs["eddsa_privkey"] = eddsa_privkey
    elif eddsa_privkey_f is not None:
        eddsa_privkey_f.seek(0)
        signer_kwargs["eddsa_privkey"] = eddsa_privkey_f.read().decode()
    elif eddsa_privkey_keychain and sys.platform.casefold() == "darwin":
        import sparklehub_cli.helpers.macos_keychain as keychain

        signer_kwargs["eddsa_privkey"] = keychain.read_eddsa_key_from_keychain()

    return signer_kwargs


def package_need_sign(package, signer_kwargs):
    return ("dsa_privkey" in signer_kwargs and not package.signature_dsa) or (
        "eddsa_privkey" in signer_kwargs and not package.signature_eddsa
    )


def sign_package(package, signer_kwargs, packages_api):
    print(Fore.CYAN + f'\u2B07 Downloading package "{package.slug}"...', file=sys.stderr)

    package_signer_kwargs = copy.deepcopy(signer_kwargs)

    # print(package)
    do_sign = False
    if "dsa_privkey" in package_signer_kwargs and not package.signature_dsa:
        do_sign = True
    else:
        package_signer_kwargs.pop("dsa_privkey")

    if "eddsa_privkey" in package_signer_kwargs and not package.signature_eddsa:
        do_sign = True
    else:
        package_signer_kwargs.pop("eddsa_privkey")

    if not do_sign:
        return

    try:
        signatures = sign_remote_file(package.url, **package_signer_kwargs)
    except Exception as e:
        print(Fore.RED + f"Unable to download and sign {package.url}. E: {e}", file=sys.stderr)
        return

    update_data = {}
    if SignatureType.DSA in signatures:
        update_data["signature_dsa"] = signatures[SignatureType.DSA]
    if SignatureType.EdDSA in signatures:
        update_data["signature_eddsa"] = signatures[SignatureType.EdDSA]

    packages_api.packages_partial_update(id=package.id, data=update_data)


# CLI
@click.group()
def cli():
    pass


@cli.group()
@click.option("-k", "--api-key", "api_key", envvar="SPARKLEHUB_API_KEY", required=True)
def release(api_key):
    configuration.api_key["Authorization"] = api_key


@release.command("list")
@click.option("-c", "--channel", "channel", required=True, envvar="SPARKLEHUB_CHANNEL", type=uuid.UUID)
def release_list(channel):
    print(Fore.LIGHTCYAN_EX + "Gathering release information from SparkleHub\u2728...", file=sys.stderr)

    with openapi_client.ApiClient(configuration) as api_client:
        releases_api = openapi_client.ReleasesApi(api_client)
        releases = releases_api.releases_list(channel=str(channel))

        for release_obj in releases:
            print(Fore.GREEN + release_obj.version)


@release.command("sign")
@click.option("-c", "--channel", "channel", required=True, envvar="SPARKLEHUB_CHANNEL", type=uuid.UUID)
@click.option("--dsa-privkey-file", "dsa_privkey_f", type=click.File("rb"))
@click.option("--eddsa-privkey-file", "eddsa_privkey_f", type=click.File("rb"))
@click.option("--eddsa-privkey", "eddsa_privkey", type=str)
@click.option("--eddsa-privkey-keychain", "eddsa_privkey_keychain", is_flag=True)
@click.argument("release", envvar="SPARKLEHUB_RELEASE", type=str, default="latest")
def release_sign(channel, release, dsa_privkey_f, eddsa_privkey, eddsa_privkey_f, eddsa_privkey_keychain):
    signer_kwargs = read_keys(
        dsa_privkey_f=dsa_privkey_f,
        eddsa_privkey=eddsa_privkey,
        eddsa_privkey_f=eddsa_privkey_f,
        eddsa_privkey_keychain=eddsa_privkey_keychain,
    )

    print(Fore.LIGHTCYAN_EX + "Gathering release information from SparkleHub\u2728...", file=sys.stderr)

    with openapi_client.ApiClient(configuration) as api_client:
        releases_api = openapi_client.ReleasesApi(api_client)
        if release == "latest":
            releases = releases_api.releases_latest(channel=str(channel))
            if len(releases) == 0:
                print(Fore.LIGHTRED_EX + "No releases so far", file=sys.stderr)
                exit(1)
            print(Fore.LIGHTCYAN_EX + f"Latest release: {releases[0].version}", file=sys.stderr)
        elif release == "all":
            releases = releases_api.releases_list(channel=str(channel))
        else:
            releases = [releases_api.releases_read(channel=str(channel), id=release)]

        packages_api = openapi_client.PackagesApi(api_client)

        for release_obj in releases:
            print(Fore.LIGHTYELLOW_EX + f'--- Release "{release_obj.title}"')
            packages = packages_api.packages_list(release=release_obj.id)

            # pprint(packages)

            packages_to_sign = list(filter(lambda x: package_need_sign(x, signer_kwargs), packages))

            if len(packages_to_sign) == 0:
                print(Fore.LIGHTGREEN_EX + f'Release "{release_obj.version}" has all packages signed')

            print(Fore.LIGHTYELLOW_EX + f'Release "{release_obj.version}" has {len(packages_to_sign)} packages to sign')

            for i, package in enumerate(packages_to_sign, start=1):
                sign_package(package, signer_kwargs, packages_api)


@cli.command()
@click.option("-f", "--privkey-file", "dsa_privkey_f", required=True, type=click.File("rb"))
@click.argument("package", required=True, type=click.File("rb"))
def sign_dsa(dsa_privkey_f, package):
    signer_kwargs = read_keys(dsa_privkey_f=dsa_privkey_f)
    print(sign_file(package, **signer_kwargs)[SignatureType.DSA])


@cli.command()
@click.option("-f", "--privkey-file", "eddsa_privkey_f", type=click.File("rb"))
@click.option("-s", "--privkey", "eddsa_privkey", type=str)
@click.option("-k", "--privkey-keychain", "eddsa_privkey_keychain", is_flag=True)
@click.argument("package", required=True, type=click.File("rb"))
def sign_eddsa(package, eddsa_privkey_f, eddsa_privkey, eddsa_privkey_keychain):
    signer_kwargs = read_keys(
        eddsa_privkey_f=eddsa_privkey_f, eddsa_privkey=eddsa_privkey, eddsa_privkey_keychain=eddsa_privkey_keychain
    )
    print(sign_file(package, **signer_kwargs)[SignatureType.EdDSA])


def main():
    colorama_init(autoreset=True)
    cli(obj={}, auto_envvar_prefix="SPARKLEHUB")


if __name__ == "__main__":
    main()
