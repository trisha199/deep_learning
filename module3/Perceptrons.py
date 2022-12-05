#!/usr/bin/env python
# coding: utf-8

# # Perceptrons

# ## First simple implementation

# In[41]:

#%%

x1, x2 = 1,2
w1, w2 = 0.5, 0.9
th = 0.7


# ```
# y = 0 (x1*w1 +x2*w2) <= th
# y = 1 (x1*w1 +x2*w2) > th
# ```

# In[42]:
#%%

out = x1*w1 +x2*w2
out

# In[43]:


if out <= th:
    y = 0
else:
    y =1


# In[44]:
#%%

y


# ## Logic Gate

# ## And gate
#%%
# In[45]:


def do_and(x1, x2):
    w1, w2 =0.5 ,0.5
    #w1 =0.5
    #w2 =0.5
    th =0.8
    
    y = x1*w1 + x2*w2
    if y <= th:
        return 0
    else:
        return 1
    


# In[46]:


def do_and2(x1, x2):
    w1, w2 =0.5 ,0.5
    #w1 =0.5
    #w2 =0.5
    th =0.8
    
    y = x1*w1 + x2*w2
    #if y <= th:
    #    return 0
    #else:
    #    return 1
    return 0 if y <= th else 1


# #### Test `do_and()`

# In[47]:


do_and(1,1)


# In[48]:


do_and(1,0)


# In[49]:


do_and(0,0)


# In[ ]:




