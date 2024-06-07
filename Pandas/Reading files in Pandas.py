#!/usr/bin/env python
# coding: utf-8

# # Reading files in Pandas

# In[1]:


import pandas as pd


# In[24]:


df = pd.read_csv(r"/Users/Joshua/Downloads/countries of the world.csv")

df


# In[23]:


df = pd.read_csv(r"/Users/Joshua/Downloads/countries of the world.txt", sep = '\t')

df


# In[7]:


#alternatively


# In[25]:


df = pd.read_table(r"/Users/Joshua/Downloads/countries of the world.txt")

df


# In[11]:


#CSV with method for Text files


# In[26]:


df = pd.read_table(r"/Users/Joshua/Downloads/countries of the world.csv", sep = ',')

df


# In[12]:


#JSON files


# In[22]:


df = pd.read_json(r"/Users/Joshua/Downloads/json_sample.json")

df


# In[ ]:





# In[28]:


df2 = pd.read_excel(r"/Users/Joshua/Downloads/world_population_excel_workbook.xlsx", sheet_name = 'Sheet1')

df2


# In[21]:


pd.set_option('display.max.rows', 235)
pd.set_option('display.max.columns', 40)


# In[32]:


df2.info()


# In[33]:


df2.shape


# In[41]:


df2.head()


# In[42]:


df2.tail(10)


# In[43]:


df2['Rank']


# In[48]:


df.loc[89]


# In[45]:


df.iloc[89]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




