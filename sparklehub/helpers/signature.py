import base64
import hashlib
from functools import partial
from typing import BinaryIO

FILE_BLOCK_SIZE = 1024 * 1024


def sign_dsa(f: BinaryIO, private_key: bytes) -> bytes:
    """
    Signs file-like object using a private key, formatted as a PEM file
    :param f: file-like object to be signed
    :param private_key: PEM-formatted contents of dsa_priv.pem
    :return: signature
    """
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.serialization import load_pem_private_key
    from cryptography.hazmat.primitives.asymmetric import utils

    key = load_pem_private_key(private_key, password=None, backend=default_backend())

    hasher = hashlib.sha1()
    f.seek(0)
    for block in iter(partial(f.read, FILE_BLOCK_SIZE), b""):
        hasher.update(block)

    return key.sign(hasher.digest(), utils.Prehashed(hashes.SHA1()))


def sign_dsa_b64(f: BinaryIO, private_key: bytes) -> str:
    return base64.b64encode(sign_dsa(f, private_key)).decode()


def sign_ed25519(f: BinaryIO, private_key: bytes) -> bytes:
    """
    Signs file-like object using a private key, defined in a very special way, compatible to crypto library, used by sign_update in Sparkle
    :param f: file-like object to be signed
    :param private_key: 96 bytes, concatenated private_scalar=a, sha512_right_half=RH, pubkey=A
    :return: signature
    """
    from pure25519.basic import bytes_to_clamped_scalar, Base, scalar_to_bytes

    assert len(private_key) == 96

    a_bytes, RH, public_key = private_key[:32], private_key[32:64], private_key[64:]
    a = bytes_to_clamped_scalar(a_bytes)

    r = hashlib.sha512()
    r.update(RH)
    f.seek(0)
    for block in iter(partial(f.read, FILE_BLOCK_SIZE), b""):
        r.update(block)
    r = int.from_bytes(r.digest(), "little")

    R = Base.scalarmult(r)
    R_bytes = R.to_bytes()

    RAM_hashed = hashlib.sha512()
    RAM_hashed.update(R_bytes)
    RAM_hashed.update(public_key)
    f.seek(0)
    for block in iter(partial(f.read, FILE_BLOCK_SIZE), b""):
        RAM_hashed.update(block)
    RAM_hashed = int.from_bytes(RAM_hashed.digest(), "little")

    S = r + RAM_hashed * a

    return R_bytes + scalar_to_bytes(S)


def sign_ed25519_b64(f: BinaryIO, private_key: str) -> str:
    return base64.b64encode(sign_ed25519(f, private_key=base64.b64decode(private_key))).decode()
