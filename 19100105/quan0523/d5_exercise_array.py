#参考同学的代码

a =[0,1,2,3,4,5,6,7,8,9]
a.reverse()
print(a)  
 
b=str(a[0])  
for i in range(1,10):
    b+=str(a[i])
print(b)

c=b[2:8]
print(c)   

d=''.join(c[i] for i in range(len(c)-1,-1,-1))
print(d)

e=int(d)
print(e)

print(bin(e),oct(e),hex(e)) 