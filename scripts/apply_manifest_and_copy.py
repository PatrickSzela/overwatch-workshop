#!/usr/bin/env python3

import subprocess
import sys

from apply_manifest import apply_manifest


def main():
    try:
        result = apply_manifest()
        subprocess.run(["wl-copy"], input=result.encode(), check=True)
        print("Workshop code copied to clipboard")
    except subprocess.CalledProcessError:
        sys.exit("Error: wl-copy failed. Is wl-clipboard installed?")


if __name__ == "__main__":
    main()
