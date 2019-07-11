a=[0,1,2,3,4,5,6,7,8,9]
b=list(reversed(a))
c=[str(i) for i in b]
d=c[2:8]
e=d[::-1]
m=[str(i) for i in e]
str1 = "".join(m)
f=int(str1)
f1= bin(f)
f2= oct(f)
f3 = hex(f)
print(f1)
print(f2)
print(f3)

