#!/usr/bin/env python
# coding: utf-8

# In[22]:


def convert_seconds(t):
    h = int((t % 3600) // 60)
    m = int((t % 3600) % 60)
    return '%i hour%s, %i minute%s' % (h, 's' if h != 1 else '', 
                                                    m, 's' if m != 1 else '')
                                                    


# In[24]:


print(convert_seconds(133))


# In[ ]:




