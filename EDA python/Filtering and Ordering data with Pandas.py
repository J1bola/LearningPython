#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"/Users/Joshua/Downloads/world_population.csv")
df


# In[6]:


df[df['Rank'] < 10]


# In[7]:


specific_countries = ['Bangladesh', 'Brazil']
df[df['Country'].isin(specific_countries)]


# In[ ]:





# In[8]:


df[df['Country'].str.contains('United')]


# In[ ]:





# In[9]:


df2 = df.set_index('Country')
df2


# In[12]:


df2.filter(items = ['Continent', 'CCA3'], axis = 1)


# In[ ]:





# In[13]:


df2.filter(items = ['Zimbabwe'], axis = 0)


# In[ ]:





# In[15]:


df2.filter(like = 'United', axis = 0)


# In[ ]:





# In[16]:


df2.loc['United States']


# In[17]:


df2.iloc[3]


# In[ ]:





# In[18]:


#ORDER BY


# In[19]:


df


# In[31]:


df[df['Rank'] < 10].sort_values(by = ['Continent','Country'], ascending = [False, True])


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




