list1=[0,1,2,3,4,5,6,7,8,9]
list1.reverse()
list2=[str(x) for x in list1]
a=''.join(list2)
b=a[3:9]
d=b[::-1]
e=int(d)

f=bin(e)
g=oct(e)
h=hex(e)
print(f)
print(g)
print(e)
