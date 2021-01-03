#!/usr/bin/env python
# coding: utf-8
#x1 + x2 + x3 + x4 <= 50
#3x1 + 2x2 + x3 <= 100
#x2 + 2x3 <=90

#x1,x2,x3,x4 >=0

# In[1]:


from scipy.optimize import linprog


# In[3]:

fiff
obj =[-20,-12,-40,-25]


# In[4]:


lhs_ineq=[[1,1,1,1],
          [3,2,1,0],
          [0,1,2,3]]


# In[6]:


rhs_ineq=[50,
          100,
          90]


# In[9]:


opt=linprog(c=obj,A_ub=lhs_ineq,b_ub=rhs_ineq,
            method="revised simplex")


# In[10]:


opt


# In[ ]:




