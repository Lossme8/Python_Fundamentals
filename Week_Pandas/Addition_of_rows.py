# Add new rows to a DataFrame using the append function
# This will append the rows at the end

import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
df = df.append(df2)
print(df)
