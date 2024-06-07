#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[8]:


df = pd.read_csv(r"/Users/Joshua/Downloads/Ice Cream Ratings.csv")
df = df.set_index('Date')
df


# In[58]:


print(plt.style.available)
plt.style.use('dark_background')


# In[59]:


df.plot(kind = 'line', figsize = (5,2))


# In[13]:


df.plot(kind = 'line', subplots = True)


# In[14]:


df.plot(kind = 'line', title = 'Ice Cream Ratings')


# In[15]:


df.plot(kind = 'line', title = 'Ice Cream Ratings', xlabel = 'Daily Ratings', ylabel = 'Scores')


# In[28]:


df.plot(kind = 'bar', stacked = True)


# In[18]:


df.plot.barh(stacked = True)


# In[24]:


df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 100, c = 'Indigo')


# In[ ]:





# In[32]:


df.plot.hist(bins =30)


# In[42]:


df.plot.area(figsize = (10,5))


# In[ ]:





# In[48]:


df.plot.pie(y = 'Flavor Rating', figsize = (12,10))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




