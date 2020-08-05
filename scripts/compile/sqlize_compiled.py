#!/usr/bin/env python3
from sys import path as syspath; syspath.append('./scripts')
from utils.mylog import *
from utils.mydb import connect_to_db, create_tables, count_rows
from utils.myfiler import get_latest_snapshot_dir

from collections import defaultdict
import csv
from pathlib import Path
import re
from sys import argv

TARGET_DB_PATH = Path('data/compiled/osha_compiled.sqlite')

CREATE_PATH = Path('scripts/compile/create_compiled_schema.sql')
INDEXES_PATH = Path('scripts/compile/index_compiled.sql')

SKIPPED_FILES = ('data_dictionary', 'metadata',)




def insert_from_csv(connection, src_path):
    NULL_CELL_COUNT = 0
    NULL_ROW_COUNT = 0

    def _convert_blank_to_null(iterdata):
        """
        every cell is expected to be a string
        """
        nonlocal NULL_CELL_COUNT
        nonlocal NULL_ROW_COUNT
        for row in iterdata:
            _row_nulled = False
            for i, v in enumerate(row):
                val = v.strip()
                if not val:
                    row[i] = None
                    NULL_CELL_COUNT += 1
                    if _row_nulled is False:
                        _row_nulled = True
                        NULL_ROW_COUNT += 1
                else:
                    row[i] = val
            yield row

    def _get_insert_statement(tablename, fields):
        fields_qstr = ', '.join(fields)
        vals_qstr = ', '.join('?' for f in fields)
        return f"INSERT INTO {tablename}({fields_qstr}) VALUES ({vals_qstr})"

    def _get_table_name(path):
        """
        path can be anything from:
            osha_violation.csv
            to: osha_violation-004.csv

        Returns:
            violation
        """
        mx = re.match(r'osha_(\w+)(?:-\d+)?', path.stem)
        return mx.groups()[0]

    # ---------------------------------------------------------
    mylog(src_path.name, src_path.parent, label="Reading")
    srcfile = src_path.open()
    records = csv.reader(srcfile)

    tablename = _get_table_name(src_path)
    fieldnames = next(records)
    mylog(tablename, label="Inserting into table")

    iq = _get_insert_statement(tablename, fieldnames)
#    myinfo(iq, label="INSERT query")
    xrecords = _convert_blank_to_null(records)

    # cursor = connection.cursor()
    # cursor.executemany(iq, xrecords)
    # myinfo(f"{count_rows(cursor, tablename)} rows in table: {tablename}", label="Row count")

    with connection as conn:  # context helper provides MASSIVE speed boost
        cursor = conn.cursor()
        cursor.executemany(iq, xrecords)

        myinfo(f"{count_rows(cursor, tablename)} rows in table: {tablename}", label="Row count")




    myinfo(NULL_ROW_COUNT, label="Empty rows NULLED")
    myinfo(NULL_CELL_COUNT, label="Empty cells NULLED")

    srcfile.close()




def main(src_dir):

    def _get_data_paths(src_dir):
        paths = sorted(p for p in src_dir.rglob('*.csv')
                        if all(_sk not in p.name
                        for _sk in SKIPPED_FILES))
        # return [p for p in paths if 'violation_event' in  p.name]
        return paths


    def _group_data_paths(paths):
        d = defaultdict(list)
        for p in paths:
            q = p.parent.stem
            d[q].append(p)
        return d


    mylog(TARGET_DB_PATH, label="Connecting to")
    conn = connect_to_db(TARGET_DB_PATH)

    mylog("Creating tables")
    create_tables(conn, schema_path=CREATE_PATH)

    allpaths = _get_data_paths(src_dir)
    myinfo(f"{len(allpaths)} total files")
    gpaths = _group_data_paths(allpaths)
    myinfo(f"{len(gpaths.keys())} groups")

    for i, (gname, srcpaths) in enumerate(gpaths.items()):
        myinfo(f"#{i+1} Group {gname} has {len(srcpaths)} files")
        for j, path in enumerate(srcpaths):
            myinfo(f"File {j+1} of {len(srcpaths)} {path}")
            insert_from_csv(conn, path)

    conn.close()



if __name__ == '__main__':
    if len(argv) < 2:
        src_dir = get_latest_snapshot_dir().joinpath('unpacked')
    else:
        src_dir = Path(argv[1])
        if not src_dir.is_dir():
            raise ValueError(f"Expected 1st argument to be a directory: {src_dir}")

    myinfo(src_dir, label="Source dir")
    myinfo(TARGET_DB_PATH, label="Stash destination")
    main(src_dir)

