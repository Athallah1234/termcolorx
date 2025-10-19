"""
termcolorx.platform — Deteksi otomatis dukungan warna dan UTF-8 terminal.
"""

import os, sys, platform, io

class PlatformSupport:
    @staticmethod
    def enable_ansi():
        if os.name == 'nt':
            os.system("")  # Enable ANSI di Windows 10+
        return True

    @staticmethod
    def enable_utf8():
        """Pastikan terminal Python pakai UTF-8 untuk dukungan emoji & warna."""
        try:
            if sys.stdout.encoding.lower() != "utf-8":
                sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
        except Exception:
            pass
        if os.name == "nt":
            os.system("")  # Enable ANSI di Windows 10+
        return True

    @staticmethod
    def is_supported():
        if sys.stdout.isatty():
            return True
        return False

    @staticmethod
    def info():
        return {
            "os": platform.system(),
            "version": platform.version(),
            "ansi_supported": PlatformSupport.is_supported(),
            "encoding": sys.stdout.encoding
        }
