

from datetime import datetime, timedelta
from helper import get_conn_str, generate_random_order



def insert_random_orders(conn, count=3):
    cursor = conn.cursor()
    for _ in range(count):
        order_date, customer_id, amount = generate_random_order()
        order_date_str = order_date.strftime('%Y-%m-%d')  # convert datetime to string
        cursor.execute(
            'INSERT INTO "TEST_SCHEMA"."RANDOM_ORDERS" (order_date, customer_id, amount) VALUES (%s, %s, %s)',
            (order_date_str, customer_id, amount)
        )
    conn.commit()
    cursor.close()


def main():
    conn = get_conn_str()
    
    print(f"run_update.py starting to insert data to sql at {datetime.now()}...")
    insert_random_orders(conn)
    conn.close()
    print(f"successfuly uploaded data to sql from run_update.py at {datetime.now()}")

if __name__ == "__main__":
    main()
