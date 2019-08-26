#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


df=pd.read_csv('cleandata.csv',header=0,encoding = 'unicode_escape')


# In[4]:


df


# In[79]:


df_1=df['Title'].to_frame()


# In[13]:


df=df.dropna(subset=['Title'])


# In[14]:


df=df.dropna(subset=['Content'])


# In[179]:


for a in df_1['Title'][0:2]:
    l=a.split(' ')
    if '|' in l:
        l.remove('|')
    print(l)


# In[207]:


string_count(df_1['Title'][2])


# In[214]:


def string_count(x):
    n=0
    a=x.split(' ')
    if '|' in a:
        a.remove('|')
    for char in a:
        n=n+1
    return n
   


# In[93]:


df=df.reset_index()


# In[99]:


df=df.drop('index',1)


# In[ ]:


df['Content_Length'] = df['Content'].apply(string_count)


# In[240]:


df.to_csv('newdata.csv',index=False)


# In[114]:


df


# In[110]:


def relevance(x):
    count=0
    a=x.split(' ')
    i=df.loc[df['Title']==x].index[0]
    b=df['Content'][i].split(' ')
    for n in a:
        if n in b:
            count+=1
    return count
            


# In[115]:


df.loc[df['Title']=='Deadliest Catch 1509 | Tonight 9p'].index


# In[111]:


df['Relevance']=df['Title'].apply(relevance)


# In[112]:


df


# In[116]:


df.to_csv('relevance.csv',index=False)


# In[ ]:




