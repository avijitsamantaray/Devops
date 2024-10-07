
import snowflake.connector
from cryptography.hazmat.primitives import serialization
import os
import pandas as pd
import sys


# connection to SnowFlake
key=os.environ['password']
conn=snowflake.connector.connect(
        user=os.environ['uname'],
        private_key=serialization.load_pem_private_key(key, password=None) ,
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






