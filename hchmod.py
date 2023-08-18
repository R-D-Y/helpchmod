#!/usr/bin/env python3

import argparse
import sys
from contextlib import redirect_stdout

def decode_chmod(chmod_str):
    permission_dict = {
        "0": "---",
        "1": "--x",
        "2": "-w-",
        "3": "-wx",
        "4": "r--",
        "5": "r-x",
        "6": "rw-",
        "7": "rwx"
    }

    decoded = []
    for digit in chmod_str:
        if digit in permission_dict:
            decoded.append(permission_dict[digit])

    return "".join(decoded)

def print_help():
    help_text = '''
This script decodes chmod numbers and provides explanations.

Usage: hchmod.py <chmod_number>

Arguments:
  chmod_number  The chmod number to decode.

Explanation of Letters:
  r: Read - Permission to read a file.
  w: Write - Permission to modify a file.
  x: Execute - Permission to execute a file.

Example:
  hchmod.py 755
    Modus for chmod 755: rwxr-xr-x
    UGO permissions: User = rwx, Group = r-x, Others = r-x
    Umask: 022
'''
    print(help_text)

def main():
    parser = argparse.ArgumentParser(description='A script to decode chmod numbers and provide explanations.')
    parser.add_argument('chmod_number', type=str, nargs='?', help='The chmod number to decode.')
    args = parser.parse_args()

    if not args.chmod_number:
        print_help()
        sys.exit(0)

    chmod_number = args.chmod_number
    if not chmod_number.isdigit() or len(chmod_number) != 3:
        print("Invalid chmod number. Please enter a valid three-digit number.")
        sys.exit(1)

    modus = int(chmod_number)
    ugo = str(modus)[0]
    g = str(modus)[1]
    o = str(modus)[2]

    modus_desc = decode_chmod(str(modus))
    ugo_desc = decode_chmod(ugo)
    g_desc = decode_chmod(g)
    o_desc = decode_chmod(o)

    umask = 777 - modus

    print(f"Modus for chmod {chmod_number}: {modus_desc}")
    print(f"UGO permissions: User = {ugo_desc}, Group = {g_desc}, Others = {o_desc}")
    print(f"Umask: {umask}")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '--help':
        with open(sys.stdout.fileno(), 'w') as f:
            with redirect_stdout(f):
                print_help()
    else:
        main()

