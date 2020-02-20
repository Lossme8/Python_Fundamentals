# If the header is in a row other than the first, pass the row number to header. This will skip the preceding rows.
import pandas as pd
df = pd.read_csv("temp.csv", names=['a', 'b', 'c', 'd', 'e'], header=0)
print(df)
