#!/usr/bin/env python3
# -*- encode: utf8 -*-

import sys
from argparse import ArgumentParser
from pathlib import Path
from oletools.olevba import VBA_Parser, filter_vba

DEFAULT_EXTENSION='.bas'
VBA_PREFIX_CODE='Option Explicit'

def get_args():
    parser = ArgumentParser(description='Extract vba source files from an MS Office file with macro.')
    parser.add_argument('src', metavar='MS_OFFICE_FILE', type=str, help='Paths to source MS Office file or directory.')
    parser.add_argument('--dst_dir', type=str,
        help='Destination directory path to output vba source files [default: ./vba_src].')
    return parser.parse_args()

def check_regular_code(code):
    code = code.strip()
    if code == '':
        return False
    if code == VBA_PREFIX_CODE:
        return False
    return True

def main():
    args = get_args()
    src_path = Path(args.src)
    dst_dir = args.dst_dir
    if not args.dst_dir:
        dst_dir = src_path.stem

    dst_path = Path(src_path.parent).joinpath(dst_dir)
    dst_path.mkdir(parents=True, exist_ok=True)

    print('Extract vba files from {source} to Dir:{dst_dir}'.format(source=src_path.resolve(), dst_dir=dst_path.resolve()))

    vba_parser = VBA_Parser(args.src)
    for (_, _, vba_filename, vba_code) in vba_parser.extract_macros():
        vba_file = dst_path.joinpath(vba_filename + DEFAULT_EXTENSION)
        code = filter_vba(vba_code)
        if not check_regular_code(code):
            print('skip: {file}'.format(file=vba_file))
        else:
            print('extract: {file}'.format(file=vba_file.resolve()))
            vba_file.write_text(code)

if __name__ == '__main__':
    main()
