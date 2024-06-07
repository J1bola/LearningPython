#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df1 = pd.read_csv(r"/Users/Joshua/Downloads/LOTR.csv")
df1


# In[8]:


df2 = pd.read_csv(r"/Users/Joshua/Downloads/LOTR 2.csv")
df2


# In[9]:


df1.merge(df2)


# In[12]:


df1.merge(df2, how = 'inner', on = ['FellowshipID', 'FirstName'])


# In[13]:


df1.merge(df2, how = 'outer')


# In[14]:


df1.merge(df2, how = 'left')


# In[15]:


df1.merge(df2, how = 'right')


# In[17]:


df1.merge(df2, how = 'cross')


# In[18]:


#Join


# In[20]:


df1.join(df2, on = 'FellowshipID', how = 'outer', lsuffix = '_Left', rsuffix = '_Right' )


# In[ ]:





# In[23]:


df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_Left', rsuffix = '_Right', how = 'outer')
df4


# In[24]:


#concatenate


# In[33]:


pd.concat([df1,df2], join = 'outer', axis = 1)


# In[34]:


# append


# In[35]:


df1.append(df2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




