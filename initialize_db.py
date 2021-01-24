from source.sqlite_utils import TABLE_SCHEMAS, get_sqlite_conn


def initialize_db() -> None:
    conn = get_sqlite_conn()
    cursor = conn.cursor()
    for table in TABLE_SCHEMAS:
        schema = ', '.join((f'{name} {data_type}' for name, data_type in TABLE_SCHEMAS[table].items()))
        query = f'CREATE TABLE IF NOT EXISTS {table} ({schema});'
        cursor.execute(query)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    initialize_db()
