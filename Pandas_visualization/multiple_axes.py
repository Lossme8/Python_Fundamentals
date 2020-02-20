#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt

# Create a figure with four subplots and shared axes

fig,axes = plt.subplots(nrows=2,ncols=2,sharex=True,
                       sharey=True)
axes[0,0].set(title='Upper Left')
axes[0,1].set(title='Uppert Right')
axes[1,0].set(title='Lower Left')
axes[1,1].set(title='Lower Right')
print(plt.show())


# In[ ]:




