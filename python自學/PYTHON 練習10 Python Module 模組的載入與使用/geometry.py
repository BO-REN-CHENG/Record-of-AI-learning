#!/usr/bin/env python
# coding: utf-8

# In[1]:


def distance(x1,y1,x2,y2):
    return((x2-x1)**2+(y2-y1)**2)**0.5
def slope(x1,y1,x2,y2):
    return(y2-y1)/(x2-x1)


# In[2]:


try:
    get_ipython().system('jupyter nbconvert --to python geometry.ipynb')
except:
    pass


# In[ ]:




