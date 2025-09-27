import pyodbc
import datetime
from run_update import generate_random_order



def test_random_orders():
    date,cid,amount = generate_random_order()
    assert isinstance(date, datetime.date)
    assert isinstance(cid, int)
    assert isinstance(amount, float)
