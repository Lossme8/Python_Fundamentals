# Skiprows skips the number of rows specified

import pandas as pd

df =pd.read_csv("temp.csv", skiprows=2)
print(df)
