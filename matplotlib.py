#!/usr/bin/env python
# coding: utf-8

# # session 3

# ## matplotlib

# ## Visulalization

# In[51]:


import matplotlib.pyplot as plt
import numpy as np


# In[52]:


### Draw a line in a diagram from position (0,10) to position (5,150):
xpoints= np.array([0,10])
ypoints= np.array([5,150])

plt.plot(xpoints,ypoints)
plt.show()


# In[ ]:


xpoints= np.array([1,2])
ypoints= np.array([10,20])
plt.plot(xpoints,ypoints)
plt.show()


# In[ ]:


xpoints= np.array([1,6])
ypoints= np.array([5,10])
plt.plot(xpoints,ypoints)
plt.show()


# In[ ]:


ypoints=np.array([4,5])
plt.plot(xpoints,ypoints,'*')
plt.show()


# In[ ]:


xpoints=np.array([3,8,1,10,23])
plt.plot(xpoints,marker='o')
plt.show()


# In[ ]:


plt.plot(ypoints,marker='X')


# In[ ]:


ypoints=np.array([3,8,1,10])
plt.plot(ypoints,'*:r')
plt.show()


# In[ ]:


ypoints= np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=20,mec='g')
plt.show()


# In[ ]:


ypoints= np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=15)#ms: marker size
plt.show()


# In[ ]:


xpoints= np.array([3,8,1,10])
plt.plot(xpoints,marker='o',ms=15,color='red')#ms: marker size
plt.show()


# In[ ]:


ypoints= np.array([3,8,1,10])
xpoints=np.array([2,5,7,9])
plt.plot(xpoints,ypoints,marker='o',ms=15)#ms: marker size
plt.show()


# In[ ]:


ypoints= np.array([3,8,1,10])
xpoints=np.array([2,5,7,9])
plt.plot(xpoints,ypoints,marker='o',ms=15)#ms: marker size mec:marker border
plt.show()


# In[ ]:


ypoints= np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=15,mfc='r',mec='b')#ms: marker size mfc=marker face color
plt.show()


# In[ ]:


ypoints= np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=10,mfc='r',mec='hotpink',linestyle='dotted')#ms: marker size
plt.show()


# In[ ]:


ypoints= np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=15,mfc='r',mec='b',linewidth='4')
plt.show()


# In[ ]:


y1=np.array([3,5,6,7,9,22])
y2=np.array([1,2,3,4])
plt.plot(y1)
plt.plot(y2)
plt.show()


# In[ ]:


x=np.array([1,2,3,4,5,6,7])
y=np.array([11,12,13,14,15,16,17])
plt.plot(x,y)
plt.title("hello",loc="right")
plt.xlabel("ave")
plt.ylabel("cal")

plt.show()


# In[ ]:


x=np.array([1,2,3,4,5,6,7])
y=np.array([11,12,13,14,15,16,17])
plt.plot(x,y)
plt.title("hello",loc="right")
plt.xlabel("ave")
plt.ylabel("cal")
plt.grid(axis='x')#grid lines for x axis
plt.show()


# In[47]:


x=np.array([1,2,3,4,5,6,7])
y=np.array([11,12,13,14,15,16,17])
plt.plot(x,y)
plt.title("hello",loc="right")
plt.xlabel("ave")
plt.ylabel("cal")
plt.grid(axis='y')#grid lines for y axis

plt.show()


# In[48]:


x=np.array([1000,2000,3000,4000,5000])
y=np.array([10,20,30,40,50])
plt.plot(x,y,marker='o',ms=15,mfc='r',mec='b',linewidth='4')
plt.title("relationship between sq and price",loc="mid")
plt.xlabel("sqft")
plt.ylabel("price")
plt.grid(axis='y',linestyle="dotted",color="brown")
plt.show()


# # subplot

# In[54]:


x=np.array([0,1,2,3])
y=np .array ([3,8,1,10])
plt.subplot(1,2, 1)
plt.plot(x,y)
#plot 2
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplit(1,2,2)
plt.plot(x,y)
plt.show()


# In[ ]:


#for scatter
x=np.array([1,2,3,4])
y=np.array([50,60,70,80,90])
plt.bar(x,y)
plt.scatter(x,y)
mylabels=["A","b","c","d"]
plt.legend()
myexplode=[0.,1.2,2.2,4]
plt.pie(x,y,labels=mylabels,startangle=90,explode=myexplode)
plt.barh(x,y)
plt.show()

