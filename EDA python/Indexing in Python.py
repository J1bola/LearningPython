#!/usr/bin/env python
# coding: utf-8

# # Indexing

# In[2]:


import pandas as pd


# In[5]:


df = pd.read_csv(r"/Users/Joshua/Downloads/world_population.csv")
df


# In[7]:


df = pd.read_csv(r"/Users/Joshua/Downloads/world_population.csv", index_col = "Country")
df


# In[11]:


df.reset_index(inplace = True) #resetting index


# In[10]:


df


# In[ ]:





# In[15]:


df.set_index('Country', inplace = True)

df


# In[17]:


df.reset_index(inplace = True)


# In[19]:


df.set_index(['Continent','Country'], inplace = True)
df


# In[32]:


df.sort_index(ascending = False)

#pd.set_option('display.max.rows', 235)


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




