#!/usr/bin/env python
# coding: utf-8
#Max z = x+2y subject to
#2x + y <= 20
#-4x + 5y <= 10
#-x + 2y >= 2
#x + 5y = 15
#x,y >=0


# In[1]:

from scipy.optimize import linprog


# In[2]:


obj = [-1,-2]


# In[3]:


lhs_ineq=[[2,1],
         [-4,5],
         [1,-2]]


# In[13]:


rhs_ineq=[20,
         10,
          2]
         


# In[25]:


lhs_eq=[[-1,5]]


# In[26]:


rhs_eq=[15]


# In[27]:


bnd=[(0,float("inf")),
    (0,float("inf"))]


# In[28]:


opt=linprog(c=obj,A_ub=lhs_ineq,b_ub=rhs_ineq,
            A_eq=lhs_eq,b_eq=rhs_eq,bounds=bnd,
           method="revised simplex")


# In[29]:


opt


# In[ ]:




