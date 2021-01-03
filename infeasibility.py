#!/usr/bin/env python
# coding: utf-8

#Max Z=200x -300y subject to
#2x + 3y>=1200
#x + y<=400
#2x + 3/2y>=900
#x,y >= 0



# In[1]:


from scipy.optimize import linprog


# In[2]:


obj = [-200,300]


# In[3]:


lhs_ineq=[[-2,-3],
         [1,1],
         [-2,-1.5]]


# In[4]:


rhs_ineq=[-1200,
         400,
         -900]


# In[5]:


bnd=[(0,float("inf")),
    (0,float("inf"))]


# In[8]:


opt=linprog(c=obj,A_ub=lhs_ineq,b_ub=rhs_ineq,
           bounds=bnd,
           method="revised simplex")


# In[9]:


opt


# In[ ]:




