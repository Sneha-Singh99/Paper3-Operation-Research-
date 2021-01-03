#!/usr/bin/env python
# coding: utf-8
#Min z = x1 - 3x2 + 2x3 subject to

#3x1 - x2 - 3x3 <= 7
#-2x1 + 4x2 <= 12
#-4x1 + 3x2 + 8x3 <= 10

#x1,x2,x3 >= 0

# In[1]:

from scipy.optimize import linprog


# In[32]:


obj = [1,-3,2]


# In[33]:


lhs_ineq=[[3,-1,3],
         [-2,4,0],
         [-4,3,8]]


# In[34]:


rhs_ineq=[7,12,10]
         


# In[35]:


bnd=[(0,float("inf")),
     (0,float("inf")),
    (0,float("inf"))]


# In[36]:


opt=linprog(c=obj,A_ub=lhs_ineq,b_ub=rhs_ineq,
           method="revised simplex")


# In[37]:


opt


# In[ ]:




