
import snowflake.connector

import os
import pandas as pd
import sys

# connection to SnowFlake

# conn=snowflake.connector.connect(
#         user=os.environ['uname'],
#         password=os.environ['password'],
#         account=os.environ['aname'],
#         database='testing',
#         schema='testing'

# )
# cts = conn.cursor()

# Task........................................................................................
def number1():
    data = cts.execute("select * from day limit 5").fetchall()
    for row in data:
        print(row)

def number2():
        user=os.environ['uname'],
        password=os.environ['password'],
        account=os.environ['aname'],
        database='testing',
        schema='testing'
        print(user)
        print(password)
        print(account)




if __name__ == "__main__":
    number2()






