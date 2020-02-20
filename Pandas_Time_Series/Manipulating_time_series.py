import pandas as pd
import numpy as np
rng = pd.date_range('12/1/2018', periods=30,
                    freq='D')
ts = pd.DataFrame(np.random.randn(len(rng), 4),
                  index=rng, columns=['A','B','C','D'])
print("Original dataset")
print(ts)

print("Getting all valus inside a date range:",ts['2018-12-15':'2018-12-20'])