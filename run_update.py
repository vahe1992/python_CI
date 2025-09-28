import pyodbc
import random
from datetime import datetime, timedelta
from helper import get_conn_str, generate_random_order



def insert_random_orders(conn, count=3):
    cursor = conn.cursor()
    for _ in range(count):
        order_date, customer_id, amount = generate_random_order()
        cursor.execute(
            "INSERT INTO [test].[dbo].[random_orders] (order_date, customer_id, amount) VALUES (?, ?, ?)",
            order_date, customer_id, amount
        )
    conn.commit()

def main():
    conn_str = get_conn_str()
    
    conn = pyodbc.connect(conn_str)
    print(f"run_update.py starting to insert data to sql at {datetime.now()}...")
    insert_random_orders(conn)
    conn.close()
    print(f"successfuly uploaded data to sql from run_update.py at {datetime.now()}")

if __name__ == "__main__":
    main()
