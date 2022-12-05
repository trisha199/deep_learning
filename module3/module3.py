#!/usr/bin/env python
# coding: utf-8

# # Logic Gates using Numpy

# In[811]:


import numpy as np


# In[812]:


x1 =1
x2 =1
w1 = 1
w2 = 1
b = -1


# # And Gate

# In[813]:


def do_and(x1,x2):
    w =np.array([w1,w2])
    x =np.array([x1,x2])
    y = np.sum(x*w) + b
    
    return 0 if y <= 0 else 1


# ### Testing out ```do_and``` numpy function

# In[814]:


do_and(0,0)


# In[815]:


xs = [(0,0),(0,1),(1,0),(1,1)]


# In[816]:


for x in xs:
    y = do_and(x[0],x[1])
    print("If you do_and with {} and {}, you will have {}".format(x[0],x[1],y))


# ### NAND Gate

# In[817]:


x1 =1
x2 =1
w1 = -1
w2 = -1
b = 2


# In[818]:


def do_nand(x1,x2):
    w =np.array([w1,w2])
    x =np.array([x1,x2])
    y = np.sum(x*w) + b
    
    return 0 if y <= 0 else 1


# Testing Nand gate with do ```do_nand```

# In[819]:


do_nand(1,1)


# In[820]:


for x in xs:
    y = do_nand(x[0],x[1])
    print("If you do_and with {} and {}, you will have {}".format(x[0],x[1],y))


# ### OR gate

# In[821]:


x1 =2
x2 =1
w1 = 2
w2 = 2
b = -1


# In[822]:


def do_or(x1,x2):
    w =np.array([w1,w2])
    x =np.array([x1,x2])
    y = np.sum(x*w) + b
    
    return 0 if y <= 0 else 1


# Testing OR gate with do ```do_or```

# In[823]:


do_or(0,0)


# In[824]:


for x in xs:
    y = do_or(x[0],x[1])
    print("If you do_and with {} and {}, you will have {}".format(x[0],x[1],y))


# ### NOR gate

# In[825]:


x1 =2
x2 =1
w1 = -2
w2 = -2
b = 1


# In[826]:


def do_nor(x1,x2):
    w =np.array([w1,w2])
    x =np.array([x1,x2])
    y = np.sum(x*w) + b
    
    return 0 if y <= 0 else 1


# Testing NOR gate with do ```do_nor```

# In[827]:


do_nor(1,1)


# In[828]:


for x in xs:
    y = do_nor(x[0],x[1])
    print("If you do_and with {} and {}, you will have {}".format(x[0],x[1],y))


# ### XOR Gate

# In[829]:


x1 = 1
x2 = 1


# In[830]:


def do_and(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    y = np.sum(x*w) + b
    return 1 if  y > 0 else 0

def do_nand(x1,x2):
    return 1 if do_and(x1,x2) == 0 else 0

def do_or(x1,x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    y = np.sum(x*w)+ b
    return 1 if y > 0 else 0

def do_nor(x1,x2):
        return 1 if do_or(x1,x2) == 0 else 0

#Combing 2 logic gates
 
def do_xor(x1,x2):
    y1 = do_or(x1,x2)
    y2 = do_nand(x1, x2)
    y = do_and(y1, y2)
        
    return y


# ### Testing out the ```do_xor``` function

# In[831]:


do_xor(1,1)


# In[832]:


for x in xs:
    y = do_xor(x[0],x[1])
    print("If you do_xor with {} and {}, you will have {}".format(x[0],x[1],y))

