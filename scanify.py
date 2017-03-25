#!/usr/bin/env python

import os
import argparse

def get_parser():
        """Get parser of arguments"""
        parser = argparse.ArgumentParser()
        parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('-g', '--grayscale', action='store_true')
        parser.add_argument('file')#, nargs='+')
        return parser

def scanify(fn, grayscale=False):
    """Scanify a file.

    Credits http://tex.stackexchange.com/questions/94523/simulate-a-scanned-paper
    http://www.imagemagick.org/Usage/photos/#color-in

    .. warning :: required imagemagick

    """
    nfn = os.path.splitext(fn)[0] + '_scan.png'
    grayscale_cmd = ' -colorspace gray ' if grayscale else ''
    os.system('convert "' + fn + '" ' + grayscale_cmd  + ' \( +clone -blur 0x1 \) +swap -compose divide -composite -linear-stretch 5%x0% "' + nfn + '"')
    print('%s save' % nfn)
    from IPython.display import Image
    return Image(filename=nfn)

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    scanify(args.file, args.grayscale)
