l1=[0,1,2,3,4,5,6,7,8,9]
l2=l1[::-1]
print(l2 )

s1=''.join([str(i)for i in l2 ])
print (s1 )

s2=s1[2:8]
print (s2)

s3=s2[::-1]
print (s3)

s4=int(s3)
print(s4)
print(bin(s4))
print(oct(s4))
print(hex(s4)) #重新提交作业