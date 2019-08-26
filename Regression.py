#!/usr/bin/env python
# coding: utf-8

# In[19]:


import gzip
import random
import string
import numpy
from collections import defaultdict
from nltk.stem.porter import PorterStemmer


# In[2]:


path = "amazon_reviews_us_Gift_Card_v1_00.tsv"


# In[3]:


f= open(path, 'rt' ,encoding='utf8')


# In[4]:


f


# In[5]:


header = f.readline()


# In[6]:


header


# In[7]:


header=header.strip().split('\t')


# In[8]:


dataset=[]


# In[9]:


for line in f:
    fields = line.strip().split('\t')
    d = dict(zip(header, fields))
    d['star_rating']=int(d['star_rating'])
    d['helpful_votes']=int(d['helpful_votes'])
    d['total_votes']=int(d['total_votes'])
    dataset.append(d)


# In[11]:


wordcount=defaultdict(int)
punctuation=set(string.punctuation)


# In[12]:


for d in dataset:
    x=''.join([w for w in d['review_body'].lower() if not w in punctuation])
    for y in x.split():
        wordcount[y]+=1


# In[13]:


wordcount


# In[14]:


len(wordcount)


# In[26]:


count = [(wordcount[p],p) for p in wordcount]


# In[20]:


stemmer=PorterStemmer()


# In[21]:


wordcount2=defaultdict(int)


# In[22]:


for d in dataset:
    x=''.join([w for w in d['review_body'].lower() if not w in punctuation])
    for y in x.split():
        y = stemmer.stem(y)
        wordcount2[y]+=1


# In[23]:


len(wordcount2)


# In[29]:


count.sort()
count.reverse()


# In[42]:


word = [x[1] for x in count[:1000]]
wordID = dict(zip(word,range(len(word))))
wordSet=set(word)


# In[43]:


wordID


# word

# In[49]:


def feature(datum):
    feat=[0]*len(word)
    x=''.join([c for c in datum['review_body'].lower() if not c in punctuation])
    for y in x.split():
        if y in word:
            feat[wordID[y]]+=1
    feat.append(1)
    return feat


# In[50]:


random.shuffle(dataset)


# In[51]:


X=[feature(d) for d in dataset]


# In[52]:


Y=[d['star_rating'] for d in dataset]


# In[ ]:


theta,residuals,ranking,S = numpy.linalg.lstsq(X,Y)


# In[54]:


theta


# In[57]:


WordWeights=list(zip(theta,word+['offset']))


# In[58]:


WordWeights.sort()


# In[59]:


WordWeights[:10]


# In[ ]:




