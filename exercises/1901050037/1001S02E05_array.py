
# coding: utf-8

# In[26]:


array=[0,1,2,3,4,5,6,7,8,9]

array2=array[::-1]
print(array2)

str3 = ''.join(str(i) for i in array2)
print(str2)

str4=str3[2:8]
print(str4)

str5 = str4[::-1]
print(str5)

num6=int(str5)
print(type(num6))
print(num6)

num7_2=bin(num6)
print(num7_2)
num7_8=oct(num6)
print(num7_8)
num7_16=hex(num6)
print(num7_16)

