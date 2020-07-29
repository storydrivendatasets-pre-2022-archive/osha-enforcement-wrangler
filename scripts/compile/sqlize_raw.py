#!/usr/bin/env python3
# DATA_DIR='data/compiled/osha/raw'
from sys import path as syspath; syspath.append('./scripts')
from myutils import mylog, myinfo, mywarn, existed_size

import apsw
import csv
from pathlib import Path

SRC_DIR = Path('data/compiled/osha/raw')
TARGET_DB_PATH = Path('data/compiled/osha/raw.sqlite')
SCHEMA_PATH = Path('data/cached/schemas/compiled_raw_schema.sql')

SKIPPED_FILES = ('metadata', 'data_dictionary')



def create_tables(connection, schema_path=SCHEMA_PATH):
    statements = [s.strip() for s in SCHEMA_PATH.read_text().split(';')]
    # assumes each create statement is delimited by ';'
    for stmt in statements:
        # excerpt stmt to get table name
        _1stline = stmt.split('\n')[0]
        mylog(_1stline)
        connection.cursor().execute(stmt)



def import_table(connection, src_path):

    def get_table_name(path):
        return path.stem.split('osha_')[1]

    def get_insert_statement(tablename, fields):
        fields_qstr = ', '.join(fields)
        vals_qstr = ', '.join('?' for f in fields)
        return f"INSERT INTO {tablename}({fields_qstr}) VALUES ({vals_qstr})"

    mylog(src_path, label="Reading")
    tablename = get_table_name(src_path)
    mylog(tablename, label="Importing into table")

    srcfile = src_path.open()
    records = csv.reader(srcfile)
    fieldnames = next(records)

    iq = get_insert_statement(tablename, fieldnames)
    myinfo(iq, label="INSERT query")

    with connection as db:
        cursor = db.cursor()
        cursor.executemany(iq, records)
        qx = cursor.execute(f'SELECT COUNT(1) FROM "{tablename}"')
        myinfo(f"{qx.fetchone()[0]} rows in {tablename}", label="Row count")


def main():
    def connect_to_db(db_path):
        dp = Path(db_path).expanduser().as_posix()
        return apsw.Connection(dp)

    def get_data_paths(srcdir=SRC_DIR):
        paths = sorted(p for p in SRC_DIR.glob('*.csv')
                        if all(_sk not in p.name
                        for _sk in SKIPPED_FILES))
        return paths


    mylog(TARGET_DB_PATH, label="Connecting to")
    conn = connect_to_db(TARGET_DB_PATH)

    mylog("Creating tables")
    create_tables(conn)

    srcpaths = get_data_paths()
    for srcpath in srcpaths:
        import_table(conn, srcpath)

    conn.close()

if __name__ == '__main__':
    main()
