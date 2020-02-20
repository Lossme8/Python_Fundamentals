import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('-' * 10 + 'Welcome to Data-Vault Tech (PTY) Ltd ' + '-' * 10)
print('\n')
df1 = pd.DataFrame({'Chips': ['Simba', 'Lays', 'Nik Naks', 'Doritos'],
                   'Price (in Rands)': [7.50, 8.00, 4.50, 10.00],
                    'Quantity': [20, 30, 15, 10],
                    })

plt.scatter('Chips','Price (in Rands)', 'Quantity',data=df1) # passing the dictionary arguments unto scatter
plt.xlabel('Product names')
plt.ylabel('Price in Rands ')
print("-"*30 + 'Plotting scatter plot' + '-'*10)
print(plt.show())
print('\n')
