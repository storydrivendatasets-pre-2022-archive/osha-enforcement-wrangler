import apsw
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


