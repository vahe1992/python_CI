
from datetime import datetime, timedelta
from helper import get_conn_str



def main():
    conn = get_conn_str()
    cursor = conn.cursor()

    # Set the context explicitly (optional but recommended)
    cursor.execute('USE DATABASE TEST')
    cursor.execute('USE SCHEMA TEST_SCHEMA')

    # Truncate the table (Snowflake uses TRUNCATE TABLE without schema in quotes)
    cursor.execute('TRUNCATE TABLE VALIDATION')
    conn.commit()

    # Insert count from random_orders into validation
    cursor.execute('INSERT INTO VALIDATION SELECT COUNT(*) FROM RANDOM_ORDERS')
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
