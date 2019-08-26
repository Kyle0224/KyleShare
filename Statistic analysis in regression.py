#!/usr/bin/env python
# coding: utf-8

# In[17]:


import csv


# In[18]:


path="amazon_reviews_us_Gift_Card_v1_00.tsv"


# In[19]:


f=open(path)


# In[20]:


a=csv.reader(f,delimiter= '\t')


# In[21]:


header=next(a)


# In[22]:


header


# In[23]:


dataset=[]


# In[24]:


for line in a:
    d=dict(zip(header,line))
    for field in ['helpful_votes','star_rating','total_votes']:
        d[field]=int(d[field])
    for field in ['verified_purchase','vine']:
        if d[field]=='Y':
            d[field]=True
        else:
            d[field]=False
    dataset.append(d)


# In[96]:


ratings=[d['star_rating'] for d in dataset]


# In[98]:


sum(ratings)/len(ratings)


# In[99]:


ratingCounts={1:0,2:0,3:0,4:0,5:0}


# In[100]:


for d in dataset:
    ratingCounts[d['star_rating']]+=1


# In[101]:


ratingCounts


# In[41]:


from collections import defaultdict


# In[103]:


ratingCounts2=defaultdict(int)


# In[105]:


for d in dataset:
    ratingCounts2[d['star_rating']]+=1


# In[106]:


ratingCounts2


# In[114]:


ProductCount=defaultdict(int)


# In[116]:


for d in dataset:
    ProductCount[d['product_id']]+=1


# In[133]:


ProductRating=defaultdict(list)


# In[134]:


for d in dataset:
    ProductRating[d['product_id']].append(d['star_rating'])


# In[180]:


for p in ProductRating:
    averageproductrating[p]=sum(ProductRating[p])/len(ProductRating[p])


# In[186]:


topRated=[(averageproductrating[p],p) for p in averageproductrating if len(ProductRating[p])>50]


# In[188]:


topRated.sort()


# In[189]:


topRated[-10:]


# In[162]:


Counts=[(ProductCount[p],p) for p in ProductCount]


# In[160]:


Counts.sort()


# In[124]:


Counts[-1]


# In[80]:


import json
import time


# In[3]:


path='review.json'
f=open(path,'r',encoding='utf8')


# In[5]:


dataset2=[]
for a in range(50000):
    dataset2.append(json.loads(f.readline()))


# In[83]:


dataset2


# In[81]:


datasetwithvalue=[]


# In[85]:


for d in dataset2:
    d['date']
    d['timeStruct']=time.strptime(d['date'],"%Y-%m-%d %H:%M:%S")
    d['timeInt']=time.mktime(d['timeStruct'])
    datasetwithvalue.append(d)


# In[86]:


dataset2[0]


# In[87]:


datasetwithvalue


# In[104]:


import collections


# In[89]:


from collections import defaultdict


# In[92]:


weekrating = defaultdict(list)


# In[93]:


for a in datasetwithvalue:
    day = a['timeStruct'].tm_wday
    weekrating[day].append(a['stars'])


# In[95]:


weekaverage={}


# In[97]:


for d in weekrating:
    weekaverage[d]=sum(weekrating[d]) / len(weekrating[d])


# In[102]:


sorted(weekaverage.keys())


# In[105]:


weekavearges = collections.OrderedDict(sorted(weekaverage.items()))


# In[107]:


weekavearges


# In[124]:


x


# In[109]:


x=list(weekavearges.keys())


# In[125]:


y


# In[110]:


y=[weekavearges[d] for d in x]


# In[112]:


import matplotlib.pyplot as plt


# In[113]:


plt.plot(x,y)


# In[130]:


plt.ylim(3.3,3.85)
plt.bar(x,y)


# In[ ]:





# In[ ]:





# In[12]:


import numpy


# In[13]:


ratings=[d['stars'] for d in dataset2]
cool=[d['cool'] for d in dataset2]
funny=[d['funny'] for d in dataset2]
useful=[d['useful'] for d in dataset2]

ratings=numpy.array(ratings)
# In[18]:


numpy.stack([cool,funny,useful])


# In[51]:


features = numpy.stack([cool,funny,useful]).T


# In[54]:


features


# In[55]:


features=numpy.matrix(features)


# In[57]:


features


# In[58]:


features.T


# In[23]:


features.T * features


# In[61]:


2*numpy.sin(features)+3 >3


# In[74]:


abc=numpy.stack([a,b,c])


# In[75]:


abc


# In[140]:


import csv


# In[141]:


path = 'pm2.5.csv'


# In[142]:


f=open(path)


# In[143]:


a=csv.reader(f,delimiter= '\t')


# In[157]:


b=f.readline().strip().split(',')


# In[144]:


header= next(a)


# In[149]:


header


# In[145]:


next(a)


# In[146]:


dataset=[]


# In[154]:


dataset3=[]


# In[150]:


for line in a:
    d=dict(zip(header,line))
    dataset.append(d)


# In[167]:


for line2 in f:
    line2=line2.split(',')
    dataset3.append(line2)


# In[169]:


N=len(dataset3)
N


# In[ ]:


dat

