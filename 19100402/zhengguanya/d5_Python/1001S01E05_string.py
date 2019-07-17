#!/usr/bin/python
# -*- coding: UTF-8 -*-
#读取文件
file = open(r'''C:\Users\ZGY\Documents\GitHub\selfteaching-python-camp\19100402\zhengguanya\d5_Python\123''','r+',encoding="utf-8")
lines = file.readlines()
print(lines)

# print(lines) 
strr=''.join(lines)
type(strr)
print(strr)
#第一步
strr1 = strr.replace('better','worse')
print(strr1)
type(strr1)

list1 = strr.replace('better','worser').split()
print(list1)

#第二步
list_1 = "ea"
list2 = []
for i in list1:
    if 'ea' not in i:
        list2.append(i)
print(list2)
type(list2)


#第三步
str3 = []
for n in list2:
       if "a"<= n <= "z":
           str3.append(n.upper())
       elif "A" <= n <= "Z":
           str3.append(n.lower())
       else:
           str3.append(n)
print(str3)

#第四步
str3.sort()
print(str3)

