Skip to content
 
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@Evanopenlife 
Code  Issues 368  Pull requests 1  Projects 14  Wiki  Security  Pulse  Community
selfteaching-python-camp/exercises/1901010052/1001S02E05_array.py
@Luckylisa379 Luckylisa379 Create 1001S02E05_array.py
a7c7388 on 4 May
20 lines (15 sloc)  284 Bytes
    
num1=[0,1,2,3,4,5,6,7,8,9]
num2=list(reversed(num1)) #翻转
print(num1)

str=''.join(str(i)for i in num2)
print(str)

num3=str[2:8]  #字符串切片
print(num3)

result=num3[::-1]
print(result)

int(result)
print(int(result))

a=int(result)
print(bin(a))
print(oct(a))
print(hex(a))
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
