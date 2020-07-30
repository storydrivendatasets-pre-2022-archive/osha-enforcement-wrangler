#!/usr/bin/env python3
# DATA_DIR='data/compiled/osha/raw'
from sys import path as syspath; syspath.append('./scripts')
from utils.mylog import *
from utils.mydb import connect_to_db, create_tables, import_table_from_csv

from pathlib import Path
import re

SCHEMA_PATH = Path('data/cache/sql/compiled_raw_schema.sql')
SRC_DIR = Path('data/compiled/osha/raw')
TARGET_DB_PATH = Path('data/compiled/osha/raw.sqlite')

SKIPPED_FILES = ('data_dictionary', 'metadata',)




def get_data_paths():
    paths = sorted(p for p in SRC_DIR.glob('*.csv')
                    if all(_sk not in p.name
                    for _sk in SKIPPED_FILES))
#   return [p for p in paths if 'osha_vio' in  p.name]
    return paths




def main():
    mylog(TARGET_DB_PATH, label="Connecting to")
    conn = connect_to_db(TARGET_DB_PATH)

    mylog("Creating tables")
    create_tables(conn, schema_path=SCHEMA_PATH)

    srcpaths = get_data_paths()
    for srcpath in srcpaths:
        import_table_from_csv(conn, srcpath)

    conn.close()

if __name__ == '__main__':
    main()
