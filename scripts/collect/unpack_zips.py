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

DEST_DIR_MAIN = Path('data', 'collected', 'unpacked.csvs')


def main(srcdir):
    datedir = srcdir.name # srcdir is expected to be dest/to/foo/2020-07-20/
    destdir = DEST_DIR_MAIN.joinpath(datedir)

    myinfo(destdir, label="Unpacked directory")

    zipnames = list(srcdir.glob('*.zip'))
    myinfo(f"Found {len(zipnames)}", srcdir)

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
    src = Path(argv[1])
    if not src.is_dir():
        raise ValueError(f"Expected 1st argument to be a directory: {src}")
    main(src)
