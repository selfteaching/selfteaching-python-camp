num=[0,1,2,3,4,5,6,7,8,9]
num=num.reverse()

s="".join(str(i) for i in num) 
print (s)
s1=s[2:8]
s2="".join(reversed(s1))
s3=int(s2)
print(bin(s3))
print(oct(s3))
print(hex(s3))