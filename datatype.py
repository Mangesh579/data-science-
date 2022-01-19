#!/usr/bin/env python
# coding: utf-8

# # data type

# In[1]:


a="python"
type(a)


# In[2]:


b=5.2
type(b)


# In[3]:


c=3
type(c)


# In[4]:


d=3+2j
type(d)


# In[5]:


e=False
type(e)


# In[7]:


f="True"
type(f)


# In[8]:


g=True
type(g)


# # rules for naming the variable

# #### variable name should not start with number
# #### variable name does not allow nany special char other than _
# #### varibale name does not allow space
# #### case sensitive

# # data structure 

# ## list

# #### 1. allows heterogenous
# #### 2. index start from 0
# #### 3. mutable using index
# #### 4. []

# In[9]:


as_a=[12,3,'hi','as',12]
as_a


# In[12]:


type (as_a)


# In[13]:


as_a[0]


# In[14]:


as_a[10]


# In[15]:


as_a[-1]


# In[18]:


as_a[2]="hello"


# In[19]:


as_a


# In[20]:


as_a.reverse()


# In[21]:


as_a


# ## tuple

# #### like list but the only difference is it is immutable
# #### ()
# #### allows heterogenous
# #### index starts from 0 and retrieves using index

# In[22]:


tuple=('a','b',1,2,3,4)
tuple


# In[23]:


tuple[1]


# In[24]:


tuple.append(5)


# In[25]:


type(tuple)


# # set 

# #### 1. add heterogenous
# #### 2. does not allow duplicates
# #### 3. cannot access using index
# #### 4. immutable using index but it's mutable
# #### 5. ordered-first place 

# In[26]:


set={1,0,12,123,14,2,3,4,1,2,3,4,6,5,4,3,2342,24,'hi','hello','hi'}


# In[27]:


set


# In[28]:


set[2]


# In[29]:


set.remove(2)


# In[30]:


set


# In[31]:


set.add(99)


# In[32]:


set


# In[33]:


set.append(23)


# # dictionary

# #### 1. dictionary has key value pair datastructure 
# #### 2. key is unique and values can be duplicated
# #### 3. can retrive the value using key
# #### 4. can change the value using key
# #### 5. key is immutable

# In[48]:


dicti={"a":"alpha",1:"first",2:"second",3:"third",1:"fourth",5:"fifth",6:"sixth"}


# In[49]:


dicti


# In[50]:


dicti[5]="fifth"
dicti


# In[51]:


dicti[5]="foruth"


# In[52]:


dicti


# In[45]:


dicti.reverse()


# In[47]:


dicti["a"]


# In[54]:


dicti["alpha"] ### key cannot be reterived using value


# In[55]:


dicti[7]= "seventh"


# In[56]:


dicti


# In[ ]:




