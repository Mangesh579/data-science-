#!/usr/bin/env python
# coding: utf-8

# # day 2

# ### numpy:package for multidimensional array
# #### Vector (1d)
# ##### Martix (2d or 1d)

# ### create an array

# In[2]:


import numpy as np 


# In[3]:


simple_list=[6,7,9]
np.array(simple_list)


# In[4]:


arr=np.array([6,7,9])
arr


# In[6]:


list_of_lists=[1,2,3],[4,5,6],[7,8,9]
np.array(list_of_lists)


# In[7]:


np.arange(10,32)


# In[8]:


np.arange(10,83,8)


# In[9]:


np.zeros(6)


# In[10]:


np.zeros(6,dtype=int)


# In[11]:


np.ones(5)


# In[12]:


np.ones(5,dtype=int)


# In[13]:


np.linspace(0,1,5)


# In[14]:


np.eye(5,dtype=int)


# In[15]:


np.ones((2,5))


# In[16]:


np.ones((2,6),dtype=int)


# In[17]:


np.random.rand(2,4)


# In[18]:


np.random.randn(2,4)


# In[19]:


np.random.rand(2,5)


# In[20]:


np.random.randint(0,10,15)


# In[21]:


sample_array=np.arange(2,20)


# In[22]:


sample_array


# In[23]:


np.ones((3,4))


# In[25]:


rand_array=np.random.randint(0,10,5)
rand_array


# In[26]:


sample_array.min()


# In[27]:


sample_array.argmin()


# In[28]:


rand_array.argmin()


# In[29]:


rand_array.max()


# In[30]:


sample_array.argmax()


# In[31]:


a=np.eye(5)


# In[32]:


a


# In[33]:


a=np.random.rand(2,3)
a


# In[34]:


a.T


# In[35]:


sample_array=np.arange(10,28)
sample_array


# In[38]:


sample_array=sample_array.reshape(6,3)
sample_array


# In[39]:


sample_array[5]=100
sample_array


# In[40]:


sample_array=np.arange(10,100)


# In[41]:


sample_array


# In[42]:


sample_array[2:10] #index from 2 to 10


# In[43]:


subset_sample_array=sample_array[0:7]
subset_sample_array


# In[44]:


sample_array[1:5]=1001
sample_array


# # two dimensional array

# In[45]:


import numpy as np


# In[47]:


a=np.array([[24,12,2,3],[1,2,3,4],[5,6,7,8]])
a


# In[48]:


a[2][2]


# In[49]:


a[:,3]


# In[50]:


a[1][3]


# In[51]:


a[1:3,2:4]


# In[52]:


a[1:,2:]


# In[53]:


a[2]


# In[56]:


a=np.arange(1,8)
a


# In[57]:


np.max(a)


# In[58]:


np.square(a)


# In[59]:


np.std(a)


# In[60]:


np.var(a)


# In[61]:


np.mean(a)


# In[62]:


array=np.random.randn(3,4)
array


# In[63]:


np.round(array,decimals=3)


# In[64]:


fruits=np.array(['aaple','mango','orange'])
np.unique(fruits)


# # PANDAS

# In[65]:


import pandas as pd


# In[66]:


import numpy as np


# ## pandas dataframe and indexing

# In[67]:


s=pd.Series([1,2,3,4],index=['a','b','c','d'])
s


# In[68]:


d=pd.Series([5,6,7,8],index=['e','f','g','h'])
d


# In[69]:


s+d  # it should be common otherwise its gonna show NaN


# In[72]:



df1=pd.DataFrame(np.random.rand(8,5),index='A B C D E F G H'.split(),columns='a b c d e'.split())
df1


# In[73]:


df1[['b','c','d']]


# In[74]:


df1['b']


# In[75]:


df1['e']=df1['a']+df1['b']
df1


# In[76]:


df1.drop('E')


# In[77]:


df1.drop('a',axis=1)


# In[78]:


df1.drop("A",axis=0)


# In[79]:


df1.drop(["a","b"],axis=1)


# In[81]:


df2={'ID':[101,102,103,107,176],'Name':['a','b','c','d','e'],'profit':[1,2,3,4,5]}
df=pd.DataFrame(df2)
df


# In[82]:


df.drop('ID',axis=1)


# In[83]:


df.drop(3)


# In[84]:


df['Name']


# In[85]:


df[['Name','ID']]


# In[86]:


df=pd.read_csv("innercity.csv")


# In[87]:


df.head()


# In[88]:


''' 
Assessment
1) create a null vector of size 10
2) create a null vector of size 10 but the fifth value should be on
3) create a vector with values ranging from 10 to 65
4) reverse the above vector 
5) create a 3x3 matrix with values ranging from 0 to 8
'''


# In[90]:


# 1
a=np.zeros(10)
a


# In[91]:


a=np.zeros(10)
a[4]=1
a


# In[93]:


a=np.arange(10,65)
a


# In[102]:


a=np.arange(65,9,-1)
a


# In[96]:


a=np.array([[0,1,2],[3,4,5],[6,7,8]])
a


# In[100]:


a=np.arange(0,9).reshape(3,3)
a


# In[ ]:




