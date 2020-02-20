import pandas as pd
# we will delete a column us a del function
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three': pd.Series([10,20,30],  index = ['a', 'b', 'c'])}
df = pd.DataFrame(d)
print("Our DataFrame is:\n")
print(df)
# Using del function

print("Deleting the first column using DEL function:")
del df['one']
print(df)

# Using pop function
print("Deleting another column using POP function:")
df.pop('two')
print(df)