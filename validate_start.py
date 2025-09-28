import pyodbc
import random
from datetime import datetime, timedelta
from helper import get_conn_str



def main():
    conn_str = get_conn_str()
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute(
            "TRUNCATE TABLE [test].[dbo].[validation]"
        )
    conn.commit()
    cursor.execute(
            "INSERT INTO [test].[dbo].[validation] SELECT COUNT(*) FROM [test].[dbo].[random_orders]"
        )
    conn.commit()

if __name__ == "__main__":
    main()
