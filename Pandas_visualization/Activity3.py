import pandas as pd
import numpy as np

data = {'Chips': ['Simba', 'Lays', 'Nik Naks', 'Doritos'],
        'Cooldrinks': ['Coke', 'Fanta', 'Sprite', 'Stoney'],
        'Chocolates': ['Cadbury', 'Tex', 'PS', 'Lindt'],
        'Pies': ['Pepper steak', 'Chicken', 'Vanision'],
        'Fruit': ['Pear', 'Apple', 'Orange', 'Banana', 'Grapes'],
        'Cupcakes': ['vanilla', 'chocolate', 'blueberry', 'cappuccino'],
        'Veggies': ['spinach', 'cabbage']}
print("Original data", data)
print("\nConverted data")
print(pd.Series(data))
