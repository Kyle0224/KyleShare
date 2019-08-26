#!/usr/bin/env python
# coding: utf-8

# In[25]:


path = '5year.arff'


# In[26]:


f=open(path,'r')


# In[27]:


f


# In[28]:


while not '@data' in f.readline():
    pass


# In[29]:


dataset=[]
for l in f:
    if '?' in l:
        continue
    l=l.split(',')
    value =[1] + [float(x) for x in l]
    value[-1]=value[-1]>0
    dataset.append(value)
    


# In[30]:


len(dataset)


# In[32]:


'?' in dataset


# In[34]:


sum(x[-1] for x in dataset)


# In[37]:


X = [values[:-1] for values in dataset]


# In[38]:


Y = [values[-1] for values in dataset]


# In[41]:


from sklearn import linear_model


# In[43]:


Model=linear_model.LogisticRegression()


# In[ ]:


Model.fit(X,Y)


# In[45]:


#Training and Testing


# In[46]:


import random


# In[47]:


random.shuffle(dataset)


# In[48]:


X2=[values[:-1] for values in dataset]


# In[49]:


Y2=[values[-1] for values in dataset]


# In[50]:


N=len(X2)


# In[52]:


X2_train=X2[:N//2]
X2_test=X2[N//2:]
Y2_train=Y2[:N//2]
Y2_test=Y2[N//2:]


# In[55]:


len(X),len(X2_train),len(X2_test)


# In[ ]:




