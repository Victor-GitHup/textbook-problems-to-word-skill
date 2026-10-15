#!/usr/bin/env python3
"""Check the local dependencies required by this skill."""

import importlib.util
import shutil
import sys


def main():
    missing = []
    for module, package in (("pdfplumber", "pdfplumber"),
                            ("PIL", "Pillow"),
                            ("docx", "python-docx")):
        if importlib.util.find_spec(module) is None:
            missing.append(package)
    if shutil.which("pdftoppm") is None:
        missing.append("Poppler (pdftoppm)")
    if missing:
        print("Missing: " + ", ".join(missing))
        print("Install Python packages from requirements.txt and Poppler, then retry.")
        return 1
    print("Ready: Python packages and pdftoppm are available.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
