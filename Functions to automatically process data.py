#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
df=pd.read_csv('extra_varaibles.csv')


# In[ ]:


#transfer value type to numeric
def valueto_numeric(cols):
    for col in cols:
        df[col]=pd.to_numeric(df[col])
#auto-upscale value by 1 
def index_upscale(a):
    for x in range(1,len(a.columns.values)):
        a[a.columns.values[x]].replace(1,x+1,inplace=True)


# In[ ]:


def automating(x):
    a=[]
    for cols in df:
        if cols.startswith(x):
            a.append(cols)
    df_x=df[a]
    index_upscale(df_x)
    valueto_numeric(df_x.columns.values)
    df_x[x]=df_x.sum(axis=1)
    
    return df_x


# In[ ]:


#x is a str
def automating_con(x):
    a=[]
    for cols in df:
        if x in cols:
            a.append(cols)
    df_x=df[a]
    index_upscale(df_x)
    valueto_numeric(df_x.columns.values)
    df_x[x]=df_x.sum(axis=1)
    
    return df_x

#x is a str
def automating_Que(x):
    df_test=automating_con(x)
    dfextralist.append(df_test)


# In[ ]:


#b is list
def table_generate(example_list):
    result=example_list[0][example_list[0].columns.values[-1]].to_frame()
    for x in range(1,len(example_list)):
        result=result.join(example_list[x][example_list[x].columns.values[-1]].to_frame())
    
    return result

