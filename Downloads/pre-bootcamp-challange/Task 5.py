#!/usr/bin/env python
# coding: utf-8

# In[12]:


def Area(a,b,c):  
    
    if (a < 0 or b < 0 or c < 0 or (a+b <= c) or (a+c <=b) or (b+c <=a) ):  
        print('Not a valid trianglen')  
        return
          
    s = (a + b + c) / 2
      
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('The area is %f' %area)   


# In[13]:


a = 5.6
b = 4.0
c = 5.0


# In[14]:


Area(a,b,c)


# In[ ]:




