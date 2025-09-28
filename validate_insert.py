import pyodbc
import random
from datetime import datetime, timedelta
from helper import get_conn_str



def main():
    conn_str = get_conn_str()
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM [test].[dbo].[validation]")  # Query to get data from validation table
    rows_before = cursor.fetchall()  # Fetch all rows

    cursor.execute("SELECT COUNT(*) FROM [test].[dbo].[random_orders]")  # Query to get data from validation table
    rows_now = cursor.fetchall()  # Fetch all rows

    cursor.execute(
            "TRUNCATE TABLE [test].[dbo].[validation]"
        )
    conn.commit()

    print(rows_now[0][0], rows_before[0][0])
    
    if rows_now[0][0] - 9 != rows_before[0][0]:
        raise ValueError("Data validation failed: Counts do not match expected values.")
    else:
        print("Data validation successful: Counts match expected values.")

    

if __name__ == "__main__":
    main()
