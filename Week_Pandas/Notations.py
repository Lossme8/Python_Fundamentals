import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8,4), columns=['A','B','C','D'])
print(df['A'])

print("Passing a list of values to [] to select those columns")
print(df[['A','B']])

print("="*30)
print(df[2:2])
