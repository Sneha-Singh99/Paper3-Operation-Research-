#!/usr/bin/env python
# coding: utf-8

# 
# Max z= 3x1 + 2x2
# subject to
# x1 + x2 <= 4
# x1 - x2 <= 2
# 
#  x1,x2 >= 0

# In[1]:


from scipy.optimize import linprog


# In[2]:


obj = [-3,-2]


# In[3]:


lhs_ineq=[[1,1],
         [1,-1]]


# In[4]:


rhs_ineq=[4,
           2]


# In[5]:


bnd=[(0,float("inf")),
    (0,float("inf"))]


# In[6]:


opt=linprog(c=obj,A_ub=lhs_ineq,b_ub=rhs_ineq,
           bounds=bnd,
           method="revised simplex")


# In[7]:


opt


# In[8]:


opt.fun


# In[9]:


opt.x


# In[ ]:




