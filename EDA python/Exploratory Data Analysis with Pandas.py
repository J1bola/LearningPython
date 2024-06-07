#!/usr/bin/env python
# coding: utf-8

# # EDA in Pandas
# 

# In[3]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[10]:


df = pd.read_csv(r"/Users/Joshua/Downloads/world_population.csv")
df


# In[7]:


df = pd.set_option('display.float_format', lambda x:'%.2f' % x) #changed the numbers after decimal to 2 decimal points


# In[11]:


df


# In[12]:


df.info()


# In[18]:


df.describe() #shows us all information about each columns


# In[15]:


df.isnull().sum()


# In[17]:


df.nunique() #shows unique values in the data


# In[21]:


df.sort_values(by="2022 Population", ascending = False).head(10) #ordering our data


# In[22]:


#correlations between numeric values


# In[23]:


df.corr()


# In[31]:


sns.heatmap(df.corr(), annot = True)

plt.rcParams['figure.figsize'] = (20,8)

plt.show()


# In[ ]:


#grouping data to look in to it more


# In[37]:


df.groupby('Continent').mean().sort_values(by = "2022 Population", ascending = False)


# In[35]:


df[df['Continent'].str.contains('Oceania')]


# In[ ]:





# In[50]:


df2 = df.groupby('Continent')[['1970 Population', 
        '1980 Population', '1990 Population', '2000 Population', 
        '2010 Population', '2015 Population', '2020 Population', 
        '2022 Population']].mean().sort_values(by = "2022 Population", ascending = False)
df2


# In[44]:


df.columns


# In[51]:


df3 = df2.transpose()
df3


# In[40]:


df2.plot()


# In[56]:


df3.plot() #we had to reverse the years for plot to be accurate


# In[ ]:





# In[55]:


df.boxplot(figsize =(20,10)) #this shows outliers in the data


# In[ ]:





# In[59]:


df.select_dtypes(include='number')


# In[ ]:





# In[60]:


df.select_dtypes(include='object')


# In[ ]:





# In[61]:


df.select_dtypes(include='float')


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




