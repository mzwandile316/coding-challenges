#!/usr/bin/env python
# coding: utf-8

# In[5]:


_CHAR = 26

def common(strings, n) : 

    prim = [True] * _CHAR 


    for i in range(n): 

        sec = [False] * _CHAR 

 
        for j in range(len(strings[i])): 
 
            if (prim[ord(strings[i][j]) - ord('a')]) : 
                sec[ord(strings[i][j]) -
                    ord('a')] = True


        for i in range(_CHAR): 
            prim[i] = sec[i] 


    for i in range(26): 
        if (prim[i]) : 
            print("%c " % (i + ord('a')), 
                            end = "") 

 
strings = [ "house","computers" ] 
n = len(strings) 
common(strings, n) 


# In[ ]:




