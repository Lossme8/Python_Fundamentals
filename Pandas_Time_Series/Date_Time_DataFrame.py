import pandas as pd
import numpy as np
import date_range as ex1

ts = pd.DataFrame(np.random.randn(len(ex1.rng), 4),
                  index=ex1.rng, columns=['A', 'B', 'C', 'D'])
print(ts)
