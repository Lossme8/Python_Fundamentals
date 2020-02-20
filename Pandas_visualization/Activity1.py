import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1,3,5,7,9])
print("Add two data Series")
ds = ds1 + ds2
print(ds)
print("-"*50)
print("Subtract two data series")
ds = ds1 - ds2
print(ds)
print("-"*50)
print("Multiply two data series")
ds = ds1 * ds2
print(ds)
print("-"*50)
print("Divide Series1 by Series2")
ds = ds1 / ds2
print(ds)