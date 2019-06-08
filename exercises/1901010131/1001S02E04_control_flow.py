#!/usr/bin/env python
# coding: utf-8

# In[29]:


for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(i, j, i*j), end='') #This line refer to other people' work
    print()


# In[54]:


i = 0
while i < 9:
    i += 1
    if i % 2 == 0: #if not odd number, will not go to the next step
        continue
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(i, j, i*j), end = '')
    print()

