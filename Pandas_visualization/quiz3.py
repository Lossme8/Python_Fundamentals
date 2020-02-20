import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8,4),
                  index = ['a','b','c','d','e','f','g','h'], columns=['A','B','C','D'])
# Select range of rows for all columns

print(df.loc['a':'h'])







data = {'Name':['Maruis', 'Irma', 'Sibongile', 'Zacharee'],'Yolisa':[18,35,28,42]}

df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])

print(df)