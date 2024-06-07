#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests


# In[6]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'


# In[9]:


page = requests.get(url)


# In[11]:


soup = BeautifulSoup(page.text,'html')


# In[14]:


print(soup.prettify())


# In[15]:


print(soup)


# In[ ]:





# In[18]:


soup.find_all('table')[1] #finding table


# In[21]:


soup.find('table', class_ = 'wikitable sortable') 


# In[63]:


table = soup.find_all('table')[1] #figured out what our actuable table was.


# In[23]:


print(table)


# In[ ]:





# In[34]:


world_titles = table.find_all('th')


# In[35]:


world_titles


# In[36]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[64]:


# got our data frame


# # importing pandas

# In[37]:


import pandas as pd


# In[42]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[65]:


column_data = table.find_all('tr') #linked our rows into the data frame


# In[57]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data


# In[58]:


df


# In[59]:


# export to CSV


# In[62]:


df.to_csv(r'/Users/Joshua/Downloads/companies.csv', index = False)


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




