#!/usr/bin/env python3

import subprocess
import sys

from apply_metadata import apply_metadata


def main():
    try:
        result = apply_metadata()
        subprocess.run(["wl-copy"], input=result.encode(), check=True)
        print("Workshop code copied to clipboard")
    except subprocess.CalledProcessError:
        sys.exit("Error: wl-copy failed. Is wl-clipboard installed?")


if __name__ == "__main__":
    main()
