import pandas as pd
from pandas import DataFrame
print('Pandas version: ' + pd.__version__)
d = [0,1,2,3]
print(d)
df = DataFrame(data =d)
print(df)
df = DataFrame(data=d, columns=['Revenue'])
print(df)


df =  DataFrame({'Revenue':[5,6,7]})
print(df)
df =  DataFrame({'Revenue':[5,6,7],
                 'Cost':[5.0,6.1,7.2]})
print(df)