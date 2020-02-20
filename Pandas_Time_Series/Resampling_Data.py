import pandas as pd
import numpy as np

rng = pd.date_range('12/1/2018',periods=30,freq='H')
ts = pd.DataFrame(np.random.randn(len(rng), 4),
                  index=rng,columns=['A','B','C','D'])
print("Original dataset", ts)
print("Resampled dataset")
print(ts.resample("1D").mean())

