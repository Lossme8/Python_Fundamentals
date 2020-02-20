import pandas as pd
df = pd.read_csv("winequality-red.csv")
print(df.head())
print("-"*30)
print(df.filter(["column","column","column"]))