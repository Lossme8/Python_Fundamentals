#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Example 7
import pandas as pd
import matplotlib.pyplot as plt
# Defining coordinates to be plotted on X and Y axes
# respectively

df1 = pd.DataFrame({'Chips': ['Simba', 'Lays', 'Nik Naks', 'Doritos'],
                   'Price (in Rands)': [7.50, 8.00, 4.50, 10.00],
                    'Quantity': [20, 30, 15, 10],
                    })
df2 = pd.DataFrame({'Cooldrinks': ['Coke', 'Fanta', 'Sprite', 'Stoney'],
                    'Price (in Rands)': [20.00, 18.00, 17.50, 19.50],
                    'Quantity': [20, 30, 15, 10]})

# plot lists 'x' and 'y'

plt.plot(df1,df2)

# Plot axes lables and show the plot

plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

print(plt.show())
