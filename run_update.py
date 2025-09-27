import pyodbc
import random
from datetime import datetime, timedelta

def generate_random_order():
    days_ago = random.randint(1, 30)
    order_date = datetime.now() - timedelta(days=days_ago)
    customer_id = random.randint(1, 100)
    amount = round(random.uniform(10.0, 500.0), 2)
    return order_date, customer_id, int(amount)

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
    conn_str = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-9C0956N;"
        "Database=test;"
        "Trusted_Connection=yes;"
    )
    conn = pyodbc.connect(conn_str)
    insert_random_orders(conn)
    conn.close()

if __name__ == "__main__":
    main()
