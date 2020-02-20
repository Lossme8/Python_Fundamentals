# specify the names of the header using the names argument

import pandas as pd
df = pd.read_csv("temp.csv", names=['a', 'b', 'c', 'd', 'e'])
print(df)
