arr = [0,1,2,3,4,5,6,7,8,9]
arr.reverse()
str1 = ''.join(str(i) for i in arr)
str2 = str1[3:9]
str3 = str2[::-1]
int1 = int(str3)
int2 = bin(int1)
int3 = oct(int1)
int4 = hex(int1)
print("该运算的二进制结果为:",int2)
print("该运算的八进制结果为:",int3)
print("该运算的十六进制结果为:",int4)