from typing import Set, Tuple

import csv

import sqlite3

DB_FILE_PATH = 'sqlite3.db'
TABLE_SCHEMAS = {
    'customers': {
        'id': 'int',
        'first_name': 'varchar',
        'last_name': 'varchar',
        'address': 'varchar',
        'state': 'varchar',
        'zip_code': 'int',
        'created_at': 'timestamp'
    },
    'purchases': {
        'customer_id': 'int',
        'purchase_status': 'varchar',
        'product_id': 'int',
        'product_name': 'varchar',
        'product_purchase': 'numeric',
        'created_at': 'timestamp'
    },
}


def get_sqlite_conn():
    conn = sqlite3.connect(DB_FILE_PATH)
    return conn


def initialize_db() -> None:
    conn = get_sqlite_conn()
    cursor = conn.cursor()

    for table in TABLE_SCHEMAS:
        cursor.execute(f'DROP TABLE IF EXISTS {table};')
        schema = ', '.join((f'{name} {data_type}' for name, data_type in TABLE_SCHEMAS[table].items()))
        cursor.execute(f'CREATE TABLE {table} ({schema});')

    conn.commit()
    conn.close()


def ingest_rows(table: str, rows: Set[Tuple]) -> None:
    conn = get_sqlite_conn()
    cursor = conn.cursor()

    values_string = ','.join('?' for _ in range(len(TABLE_SCHEMAS[table])))
    query = f'INSERT INTO {table} VALUES ({values_string})'
    cursor.executemany(query, rows)

    conn.commit()
    conn.close()


def ingest_csv_reader(csv_reader: csv.reader) -> None:
    customers, purchases = set(), set()
    for row in csv_reader:
        customers.add(tuple(row[:6]) + (row[-1],))
        purchases.add((row[0],) + tuple(row[6:]))

    ingest_rows('customers', customers)
    ingest_rows('purchases', purchases)
