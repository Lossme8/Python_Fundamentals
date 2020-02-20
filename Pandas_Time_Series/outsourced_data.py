import pandas as pd
df = pd.read_csv("AAPL.csv")
rng = pd.date_range(start="6/1/2017",end="6/30/2017",freq="B")
print(rng)
print("-"*30 + "-"*20)
print(df.head())
print("-"*30 + "-"*20)
rng = df.set_index(rng,inplace=True)
print(df)
%matplotlib inline 
