from datetime import datetime
from helper import get_conn_str

def main():
    conn = get_conn_str()
    cursor = conn.cursor()

    # Set session context to database and schema
    cursor.execute('USE DATABASE TEST')
    cursor.execute('USE SCHEMA TEST_SCHEMA')

    # Query rows from validation table
    cursor.execute('SELECT * FROM VALIDATION')
    rows_before = cursor.fetchall()

    # Query count from random_orders table
    cursor.execute('SELECT COUNT(*) FROM RANDOM_ORDERS')
    rows_now = cursor.fetchall()

    # Truncate validation table
    cursor.execute('TRUNCATE TABLE VALIDATION')
    conn.commit()

    print(rows_now[0][0], rows_before[0][0])

    if rows_now[0][0] - 9 != rows_before[0][0]:
        raise ValueError("Data validation failed: Counts do not match expected values.")
    else:
        print("Data validation successful: Counts match expected values.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
