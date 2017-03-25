#!/usr/bin/env python

import os
import argparse

def get_parser():
        """Get parser of arguments"""
        parser = argparse.ArgumentParser()
        # parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('files', nargs='+')
        return parser

def resize(fn):
    """resize

    .. warning :: required imagemagick
    """
    for fn in fns:
        nfn = os.path.splitext(fn)[0] + '_resized50p.png'
        os.system('convert -resize 50% "' + fn + '" "' + nfn + '"')
        print('%s save' % nfn)

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    fns = args.files
    resize(fns)
