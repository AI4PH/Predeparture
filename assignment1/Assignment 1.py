#!/usr/bin/env python
# coding: utf-8

# In[51]:


import numpy as np


# In[52]:


participants=[{'name':'Joice','sex':'female','age':'23'},{'name':'John','sex':'male','age':'42'},{'name':'Michael','sex':'male','age':'28'},{'name':'George','sex':'male','age':'51'},{'name':'Matthew','sex':'male','age':'32'},{'name':'Jessica','sex':'female','age':'38'}]


# In[53]:


print (participants)


# In[54]:


group=['no treatment','treatment']


# In[55]:


print (group)


# In[59]:


def add_label(input1):
    input1["allocation"]=group[np.random.randint(0,2)]


# In[60]:


for x in participants:
    add_label(x)


# In[61]:


print (participants)

