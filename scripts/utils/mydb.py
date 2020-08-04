import apsw
import csv
from pathlib import Path
import re
from sys import path as syspath; syspath.append('./scripts')
from utils.mylog import *

def connect_to_db(db_path):
    dp = Path(db_path).expanduser().as_posix()
    return apsw.Connection(dp)


def create_tables(connection, schema_path):
    def _parse_statements(txt):
        """
        assumes each create statement is delimited by ';'
        Returns a dict, with table names as keys, create statements as values
        """
        d = {}
        for t in txt.strip(' ;\n').split(';'):
            stmt = t.strip()
            tbl = re.search(r'CREATE TABLE[^"]*?"([^"]+)" *\(', stmt).groups()[0]
            d[tbl] = stmt
        return d

    txt = schema_path.read_text()

    for tbl, stmt in _parse_statements(txt).items():
        mylog(f'CREATE TABLE "{tbl}"...')
        connection.cursor().execute(stmt)


def count_rows(cursor, tablename):
    tbl = '.'.join(f'''"{t.strip('"')}"''' for t in tablename.split('.'))
    qx = cursor.execute(f"SELECT COUNT(1) FROM {tbl}")
    return qx.fetchone()[0]



def import_table_from_csv(connection, src_path):
    NULL_COUNT = 0

    def _convert_blank_to_null(iterdata):
        nonlocal NULL_COUNT
        for row in iterdata:
            for i, val in enumerate(row):
                if val.strip() == '':
                    row[i] = None
                    NULL_COUNT += 1
#           import pdb; pdb.set_trace()
            yield row

    def _get_insert_statement(tablename, fields):
        fields_qstr = ', '.join(fields)
        vals_qstr = ', '.join('?' for f in fields)
        return f"INSERT INTO {tablename}({fields_qstr}) VALUES ({vals_qstr})"


    def _get_table_name(path):
        return path.stem.split('osha_')[1]


    mylog(src_path, label="Reading")
    srcfile = src_path.open()
    records = csv.reader(srcfile)
    fieldnames = next(records)

    tablename = _get_table_name(src_path)
    mylog(tablename, label="Importing into table")

    iq = _get_insert_statement(tablename, fieldnames)
    myinfo(iq, label="INSERT query")

    xrecords = _convert_blank_to_null(records)
    with connection as db:
        cursor = db.cursor()
        cursor.executemany(iq, xrecords)

        myinfo(f"{count_rows(cursor, tablename)} rows in {tablename}", label="Row count")


    myinfo(NULL_COUNT, label="Empty cells NULLED")
    srcfile.close()

