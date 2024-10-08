
import snowflake.connector
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import os
import pandas as pd
import sys


# connection to SnowFlake
key=os.environ['password']
private_key= serialization.load_pem_private_key(bytes(str(key), encoding="utf-8"), password=None,backend=default_backend() )
access_key = private_key.private_bytes(
      encoding=serialization.Encoding.DER,
      format=serialization.PrivateFormat.PKCS8,
      encryption_algorithm=serialization.NoEncryption(),
)
conn=snowflake.connector.connect(
        user=os.environ['uname'],
        private_key=access_key,
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
    # number1()






