
import snowflake.connector
from dotenv import load_dotenv
import os
import pandas as pd
import sys

# connection to SnowFlake
load_dotenv()
conn=snowflake.connector.connect(
        user=os.environ['uname'],
        password=os.environ['password'],
        account=os.environ['aname'],
        database='testing',
        schema='testing'

)
cts = conn.cursor()

# Task........................................................................................
def number1():
    data = cts.execute("select * from day limit 5").fetchall()
    for row in data:
        print(row)




if __name__ == "__main__":
    number1()






