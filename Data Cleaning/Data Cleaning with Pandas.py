#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[6]:


df = pd.read_excel(r"/Users/Joshua/Downloads/Customer Call List.xlsx")
df


# In[ ]:





# In[8]:


df = df.drop_duplicates()
df


# In[ ]:





# In[9]:


df = df.drop(columns = "Not_Useful_Column")
df


# In[11]:


df["Last_Name"].str.strip()


# In[13]:


df["Last_Name"] = df["Last_Name"].str.lstrip("...")
df


# In[15]:


df["Last_Name"] = df["Last_Name"].str.lstrip("/")
df["Last_Name"] = df["Last_Name"].str.rstrip("_")

#alternatively
#df["Last_Name"] = df["Last_Name"].str.strip("123._/")


# In[ ]:





# In[8]:


df


# In[16]:


df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]', '')


# In[23]:


#df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
#df

#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

#df["Phone_Number"] = df["Phone_Number"].str.replace('nan', '')
#df["Phone_Number"] = df["Phone_Number"].str.replace('Na--', '')
#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
#df["Phone_Number"] = df["Phone_Number"].str.replace('nan--', '')
df


# In[11]:


df["Address"].str.split(',',2, expand = True) #tried splitting the address, but not quite right


# In[25]:


#df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',',2, expand = True)
df


# In[ ]:





# In[28]:


df["Paying Customer"] = df["Paying Customer"].str.replace('Yes', 'Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No', 'N')
df["Paying Customer"]


# In[29]:


df


# In[ ]:





# In[32]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N')
df["Do_Not_Contact"]


# In[33]:


df


# In[ ]:





# In[35]:


df = df.replace("N/a", "")
#df = df.replace("Na", "")
#df.replace("N/a", "")

df = df.fillna('')


# In[36]:


df


# In[37]:


df


# In[38]:


# dropping numbers that do not want them to call us


# In[39]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)
        
df


# In[ ]:





# In[ ]:


df = df.replace("Na", "")


# In[40]:


for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace=True)
        
df

# alternatively we could have done this to drop null values

# df.dropna(subset="Phone_Number", inplace=True)


# In[ ]:





# In[46]:


df = df.reset_index(drop=True)


# In[47]:


df


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




