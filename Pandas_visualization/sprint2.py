import pandas as pd
from sqlalchemy.dialects import sqlite

df = pd.read_csv('Data_Vault.csv', sep="\t")
print(df.filter(["Chips", 'Coldrinks', 'Chocolates', 'Pies', 'Cupcakes', 'Fruits', 'Veggies', ]))
conn = sqlite.connect(":memory:")
df.to_sql("whole", con=conn, index=False, if_exists="replace")
_q = 'select from * whole'
_d = pd.read_sql(_q, conn)
print(df)
