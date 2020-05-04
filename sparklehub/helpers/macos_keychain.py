from typing import Optional

from PyObjCTools.Conversion import propertyListFromPythonCollection
from Security import (
    SecCopyErrorMessageString,
    SecItemCopyMatching,
    errSecSuccess,
    kCFBooleanTrue,
    kSecAttrAccount,
    kSecAttrProtocol,
    kSecAttrProtocolSSH,
    kSecAttrService,
    kSecClass,
    kSecClassGenericPassword,
    kSecReturnData,
)


def read_eddsa_key_from_keychain() -> Optional[str]:
    query = propertyListFromPythonCollection(
        {
            kSecClass: kSecClassGenericPassword,
            kSecAttrService: "https://sparkle-project.org",
            kSecAttrAccount: "ed25519",
            kSecAttrProtocol: kSecAttrProtocolSSH,
            kSecReturnData: kCFBooleanTrue,
        }
    )
    rescode, data = SecItemCopyMatching(query, None)

    if rescode == errSecSuccess:
        return bytes(data).decode()
    else:
        raise RuntimeError(str(SecCopyErrorMessageString(rescode, None)))
