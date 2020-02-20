# This specifies in the csv file to customize the index using index_col
import pandas as pd
df = pd.read_csv("temp.csv", index_col=['S.No'])
print(df)
