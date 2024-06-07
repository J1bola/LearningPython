#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"/Users/Joshua/Downloads/Flavors.csv")
df


# In[6]:


df.groupby('Base Flavor')


# In[7]:


group_by_frame = df.groupby('Base Flavor')


# # Aggregate FN

# In[8]:


group_by_frame.mean()


# In[9]:


df.groupby('Base Flavor').mean()


# In[10]:


df.groupby('Base Flavor').count()


# In[11]:


df.groupby('Base Flavor').min()


# In[12]:


df.groupby('Base Flavor').max()


# In[13]:


df.groupby('Base Flavor').sum()


# In[15]:


df.groupby('Base Flavor').agg({'Flavor Rating':['mean', 'max', 'count', 'sum'], 'Texture Rating':['mean', 'max', 'count', 'sum'] })


# In[18]:


df.groupby(['Base Flavor', 'Liked']).mean()


# In[19]:


df.groupby(['Base Flavor', 'Liked']).agg({'Flavor Rating':['mean', 'max', 'count', 'sum']})


# In[ ]:





# In[20]:


df.groupby('Base Flavor').describe()


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




