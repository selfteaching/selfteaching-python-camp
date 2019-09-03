l = [0,1,2,3,4,5,6,7,8,9]
array1 = list(reversed(l))
str1 = "".join('%s'%id for id in array1) #遍历array1，并将列表中的数字都转化为字符串格式，数字格式无法合并成字符串
str2= "".join('%s'%id for id in array1[2:8])
l2 = list(str2)
l2 = list(reversed(l2))
str3 = "".join(l2)
str4=int(str3)
p1=bin(str4)
p2=oct(str4)
p3=hex(str4)
print(p1,p2,p3)
