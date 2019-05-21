a =[0,1,2,3,4,5,6,7,8,9]
a =a[::-1]
b ="".join(str(i) for i in a)
c =b[2:8]
c =c[::-1]
c =int(c)
print("转换为二进制结果为:",bin(c))
print("转换为八进制结果为:",oct(c))
print("转换为十六进制结果为:",hex(c))