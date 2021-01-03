#!/usr/bin/env python
# coding: utf-8
#Min z = 4x1 + x2 subjected to

#3x1 + 4x2 >= 20
#x1 + 5x2 >= 15

#x1,x2 >= 0
# In[1]:

from scipy.optimize import linprog


# In[2]:


obj = [4,1]


# In[3]:


lhs_ineq=[[-3,-4],
         [-1,-5]]


# In[4]:


rhs_ineq=[-20,
         -15]


# In[5]:


bnd=[(0,float("inf")),
    (0,float("inf"))]


# In[8]:


opt=linprog(c=obj,A_ub=lhs_ineq,b_ub=rhs_ineq,
           bounds=bnd,
           method="interior-point")


# In[12]:


opt


# In[ ]:




