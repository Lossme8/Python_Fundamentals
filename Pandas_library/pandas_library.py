import pandas as pd
df = pd.DataFrame({'Date':['7/10/19', '8/10/19', '9/10/19', '10/10/19', '11/10/19'],
                   'Hours Worked': [7, 7, 7, 7, 7],
                   ' Knowledge acquired on date in percentage': [20, 23, 17, 33 , 7]})
print(df)
print("-"*50)
print(df.tail())
print("-"*30)
print(df.head())