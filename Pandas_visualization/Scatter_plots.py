#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Example 19
# Creating a dictionary with three key-value pairs
import numpy as np
import matplotlib.pyplot as plt
dictionary = {'a':np.linspace(1,100,50),
             'c':np.random.randint(0,50,50),
             'd':np.abs(np.random.randn(50))*100}
# Creating a new dictionary key-value pair
dictionary['b'] = dictionary['a']*np.random.rand(50)
# Plotting a scatter plot using argument 'data'
plt.scatter('a','b',c='c',s='d',data=dictionary)

# Labelling the plot and showing it
plt.xlabel('A Data Points')
plt.ylabel('B Data Points')
plt.show()


