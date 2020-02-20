# dtype of the column can be passed as a dict

import pandas as pd
import numpy as np
df = pd.read_csv("temp.csv", dtype={'Salary':np.float64})
print(df.dtypes)
print(df)
