import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('-' * 10 + 'Welcome to Data-Vault Tech (PTY) Ltd ' + '-' * 10)
print('\n')
df1 = pd.DataFrame({'Chips': ['Simba', 'Lays', 'Nik Naks', 'Doritos'],
                   'Price (in Rands)': [7.50, 8.00, 4.50, 10.00],
                    'Quantity': [20, 30, 15, 10],
                    })
df2 = pd.DataFrame({'Cooldrinks': ['Coke', 'Fanta', 'Sprite', 'Stoney'],
                    'Price (in Rands)': [20.00, 18.00, 17.50, 19.50],
                    'Quantity': [20, 30, 15, 10]})
df3 = pd.DataFrame({ 'Chocolates': ['Cadbury', 'Tex', 'PS', 'Lindt'],
                   'Price (in Rands)': [14.50, 8.0, 11.00, 45.00],
                   'Quantity': [20, 30, 15, 10],
                   })
df4 = pd.DataFrame({'Pies': ['Pepper steak', 'Chicken', 'Vanision', 'spinach&feta'],
                   'Price (in Rands)': [21.50, 18.00, 29.50, 12.00],
                   'Quantity': [20, 30, 15, 10],
                   })
df5 = pd.DataFrame({ 'Fruit': ['Pear', 'Apple', 'Orange', 'Banana', ],
                   'Price (in Rands)': [17.85, 18.90, 12.00, 13.50],
                   'Quantity': [20, 30, 15, 10],
                  })
df6 = pd.DataFrame({ 'Cupcakes': ['vanilla', 'chocolate', 'blueberry', 'cappuccino'],
                   'Price (in Rands)': [30.00, 25.40, 42.50, 23.50],
                   'Quantity': [20, 30, 15, 10],
                  })
df7 = pd.DataFrame({ 'Veggies': ['spinach', 'cabbage', 'potato', 'peppers'],
                   'Price (in Rands)': [12.00, 9.50, 16.00, 28.00],
                   'Quantity': [20, 30, 15, 10],})

print('-'*10 + "Welcome to our CHIPS shelf" + '-'*10 + "what would you like to buy?\n")
print(df1)
#print("-"*100)
print('\n' + '-'*10 + "Welcome to our COLDRINKS shelf" + '-'*10 + "what would you like to buy?\n")
print(df2.filter(['Cooldrinks']))
print('\n' + '-'*10 + "Welcome to our CHOCOLATES shelf" + '-'*10 + "what would you like to buy?\n")
print(df3)
print('\n' + '-'*10 + "Welcome to our COLDRINKS shelf" + '-'*10 + "what would you like to buy?\n")
print(df4)
print('\n' + '-'*10 + "Welcome to our FRUITS shelf" + '-'*10 + "what would you like to buy?\n")
print(df5)
print('\n' + '-'*10 + "Welcome to our CUPCAKES shelf" + '-'*10 + "what would you like to buy?\n")
print(df6)
print('\n' + '-'*10 + "Welcome to our VEGGIES shelf" + '-'*10 + "what would you like to buy?\n")
print(df7)

