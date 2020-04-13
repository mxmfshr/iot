import sqlite3
import pandas as pd

conn = sqlite3.connect('./db.sqlite')
cursor = conn.cursor()

query = "SELECT * FROM USERS"

res = cursor.execute(query)

df = pd.DataFrame(res, columns=['id','card_id','card_text','last_used','status'])
print(df)

cursor.close()
