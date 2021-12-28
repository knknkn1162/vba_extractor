#!/usr/bin/env python3
# -*- encode: utf8 -*-

import sys
from argparse import ArgumentParser
from pathlib import Path
from oletools.olevba import VBA_Parser, filter_vba


def get_args():
    parser = ArgumentParser(description='Extract vba source files from an MS Office file with macro.')
    parser.add_argument('src', metavar='MS_OFFICE_FILE', type=str, help='Paths to source MS Office file or directory.')
    parser.add_argument('--dst_dir', type=str,
        help='Destination directory path to output vba source files [default: ./vba_src].')
    return parser.parse_args()

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
        vba_file = dst_path.joinpath(vba_filename + '.vba')
        print('output: {file}'.format(file=vba_file))
        vba_file.write_text(filter_vba(vba_code))

if __name__ == '__main__':
    main()
