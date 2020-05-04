import enum
import sys


class Platform(enum.Enum):
    WINDOWS = "windows"
    WINDOWS_X86 = "windows-x86"
    WINDOWS_X64 = "windows-x64"
    MACOS = "macos"

    @classmethod
    def get_current(cls):
        if sys.platform == "win32":
            return cls.WINDOWS
        if sys.platform == "darwin":
            return cls.MACOS
        return None

    @classmethod
    def get_current_str(cls):
        p = cls.get_current()
        return p.value if p else None


class WindowsInstaller(enum.Enum):
    INNOSETUP = "innosetup"
    MSI = "msi"
    NSIS = "nsis"


class SignatureType(enum.Enum):
    EdDSA = enum.auto()
    DSA = enum.auto()
