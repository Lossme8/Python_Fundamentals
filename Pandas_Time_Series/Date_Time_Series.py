import numpy as np
import pandas as pd
import date_range as ex1
ts = pd.Series(np.random.randn(len(ex1.rng)), index=ex1.rng)