import apsw
from pathlib import Path
import re
from sys import path as syspath; syspath.append('./scripts')
from utils.mylog import *


CREATE_TABLE_DELIMITER = ';;--'
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
        create_stmts = [s.strip('\n ') for s in txt.split(CREATE_TABLE_DELIMITER)]
        create_stmts = [s for s in create_stmts if s]

        for t in create_stmts:
            stmt = t.strip()
            tbl = re.search(r'CREATE TABLE[^"]*?"([^"]+)" *\(', stmt).groups()[0]
            d[tbl] = stmt
        return d

    txt = schema_path.read_text()
    statements = _parse_statements(txt)

    myinfo(f"Read {len(statements.keys())} create table statements")

    for tbl, stmt in statements.items():
        mylog(f'CREATE TABLE "{tbl}"...')
        connection.cursor().execute(stmt)


def count_rows(cursor, tablename):
    tbl = '.'.join(f'''"{t.strip('"')}"''' for t in tablename.split('.'))
    qx = cursor.execute(f"SELECT COUNT(1) FROM {tbl}")
    return qx.fetchone()[0]


