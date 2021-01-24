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

