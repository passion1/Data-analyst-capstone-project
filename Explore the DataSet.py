#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"


# In[5]:


df = pd.read_csv(dataset_url)


# In[6]:


df.head()


# In[7]:


print(len(df))


# In[8]:


print(len(df.columns))


# In[10]:


df.dtypes


# In[11]:


df["Age"].mean()


# In[12]:


n = len(pd.unique(df['Country']))
print("Number of Unique Countries :", n)


# In[ ]:




