df2 =  DataFrame({'Revenue':[5,6,7]})
df = df.append(df2, ignore_index=True, sort = False)
print(df)