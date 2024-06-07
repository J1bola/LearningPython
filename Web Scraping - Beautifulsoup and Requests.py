#!/usr/bin/env python
# coding: utf-8

# # Python tutorial continues wirh Alex Fredberg

# In[ ]:





# # Web Scraping - Beautifulsoup and Requests

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://www.scrapethissite.com/pages/forms/'


# In[5]:


page = requests.get(url)


# In[8]:


soup = BeautifulSoup(page.text, 'html')


# In[9]:


print(soup)


# In[10]:


print(soup.prettify())


# In[ ]:





# # Find and Find_all - digging in to the web page

# In[11]:


print(soup)


# In[ ]:





# In[12]:


soup.find('div')


# In[14]:


soup.find_all('div') # specifies all div tags


# In[ ]:





# In[15]:


soup.find_all('div', class_ = 'col-md-12')


# In[ ]:





# In[16]:


soup.find_all('p')


# In[30]:


soup.find_all('p', class_ = 'lead')


# In[ ]:





# In[19]:


soup.find_all('p', class_ = 'lead').text #find all does not allow for text; only find does.#


# In[20]:


soup.find('p', class_ = 'lead').text


# In[24]:


soup.find('th').text.strip()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




