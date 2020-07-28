#!/usr/bin/env python

"""
collect/unpack_zips.py

Requires one argument, expects it to be a directory:

    ./collect/unpack_zips.py data/collected/zips/2020-07-27
"""
from sys import path as syspath; syspath.append('./scripts')


from myutils import mylog, myinfo, mywarn, existed_size
from pathlib import Path
import re
from sys import argv
from zipfile import ZipFile

DATA_DIR = Path('data', 'collected', 'osha',)


def main(srcdir, destdir):

    zipnames = list(srcdir.glob('*.zip'))
    myinfo(f"Found {len(zipnames)} zipfiles")

    for zn in zipnames:
        # we actually make a subdir for each zip file
        _zsub = re.search(r'(\w+)_\d{8}', zn.stem).groups()[0]
        zdir = destdir.joinpath(_zsub)
        zdir.mkdir(exist_ok=True, parents=True)
        z = ZipFile(zn)
        for fname in z.namelist():
            destpath = z.extract(fname, path=zdir)
            mylog(destpath, f"{existed_size(destpath)} bytes", label="Extracted")




if __name__ == '__main__':
    if len(argv) < 2:
        # assume data/collected/2020-07-27 (i.e. latest dir) is the working
        # directory
        datadirs = [p for p in DATA_DIR.glob('*/zips/') if p.is_dir() and re.search(r'\d{4}-\d{2}-\d{2}', str(p))]
        if not datadirs:
            raise ValueError(f"Could not find any valid collected zip directories in {DATA_DIR}")
        else:
            srcdir = sorted(datadirs)[-1]
    else:
        srcdir = Path(argv[1])
        if not srcdir.is_dir():
            raise ValueError(f"Expected 1st argument to be a directory: {srcdir}")
    myinfo(srcdir, label="Source dir")

    datedir = srcdir.parent.name # srcdir is expected to be dest/to/foo/2020-07-20/zips
    destdir = DATA_DIR.joinpath(datedir, 'unpacked')
    myinfo(destdir, label="Unpacked destination")

    main(srcdir, destdir)
