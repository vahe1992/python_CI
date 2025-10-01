import pyodbc
import random
from datetime import datetime, timedelta
import snowflake.connector

def generate_random_order():
    days_ago = random.randint(1, 30)
    order_date = datetime.now() - timedelta(days=days_ago)
    customer_id = random.randint(1, 100)
    amount = round(random.uniform(10.0, 500.0), 2)
    return order_date, customer_id, amount

def get_conn_str():
    return (snowflake.connector.connect(
    ))



# conn = get_conn_str()
