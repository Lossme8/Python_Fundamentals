#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Example 23
# Data values for creating a histogram
import matplotlib.pyplot as plt
y = [95, 42, 69, 11, 49, 32, 74, 62, 25, 32]

# Creating a histogram

plt.hist(y)
plt.xlabel('Bins')
plt.ylabel('Frequency')
print(plt.show())


# In[4]:


# Example 24
plt.hist(y,bins=20)
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.show()


# In[6]:


# Example 25
# Creating an array
import numpy as np
array = np.random.normal(0, 1, 10000)

# Creating a histogram
plt.hist(array)
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.show()


# In[7]:


# -Example 26-

# Creating an array

array = np.random.normal(0, 1, 10000)

# Creating a histogram and plotting it

plt.hist(array, color='purple', histtype='step')
plt.xlabel('Bins')

plt.ylabel('Frequency')

plt.show()


# In[8]:


# -Example 27-

# Creating an array

array = np.random.normal(0, 1, 10000)

# Creating a histogram and plotting it

plt.hist(array, color='teal', orientation='horizontal')

plt.xlabel('Frequency')

plt.ylabel('Bins')

plt.show()


# In[12]:


# -Example 28: Technique 1-
import pandas as pd
# Creating a histogram using a dataframe method
data = pd.read_csv('https://bit.ly/2WcsJE7', index_col=0,
                   parse_dates=True)
data['Volume'].plot(kind='hist')

plt.show()


# In[13]:


# -Example 28: Technique 2-

plt.hist(data['Volume'])

plt.ylabel('Frequency')

plt.show()


# In[14]:


# -Example 29-

# Extracting close prices from the dataframe

close_prices = data['AdjClose']

# Plotting the close prices

plt.plot(close_prices)

plt.show()


# In[15]:


# -Example 30-

plt.plot(close_prices)

# Rotating the values along x-axis to 45 degrees

plt.xticks(rotation=45)

plt.show()


# In[16]:


# -Example 31-

# Creating a figure with the size 10 inches by 5 inches
fig = plt.figure(figsize=(10, 5))

plt.plot(close_prices)

plt.show()


# In[21]:


# -Example 32-

# Creating a figure, setting its size and plotting close

# prices on it

fig = plt.figure(figsize=(10, 5))

plt.plot(close_prices, color='purple')

# Customizing the axes

plt.xticks(rotation=45, color='teal', size=12)

plt.yticks(rotation=45, color='teal', size=12)

# Setting axes labels
plt.title('AAPL Close Prices', color='purple', size=20)
plt.xlabel('Dates', {'color': 'orange', 'fontsize':15})

plt.ylabel('Prices', {'color': 'orange', 'fontsize':15})
plt.grid(True)
plt.show()


# In[18]:


# -Example 33-

# Showing legends and setting the title of plot

plt.legend()

plt.title('AAPL Close Prices', color='purple', size=20)


# In[19]:


# -Example 34-

# Adding the grid to the plot

plt.grid(True)


# In[22]:


#!/usr/bin/python
import MySQLdb




import MySQLdb


# In[ ]:




