first = [0,1,2,3,4,5,6,7,8,9]
second = list(reversed(first))   #翻转a
print(second)

str = ''.join(str(i) for i in second)   #翻转后的数组拼接成字符串
print(str)

third = str[2:8]   #用字符串切片的方式取出第三到第八个字符
print(third)

result = third[::-1]   #翻转字符串
print(result)

int(result)   #转换成int
print(int(result))

dec = int(result)
print(bin(dec))   #转换成二进制
print(oct(dec))   #转换成八进制
print(hex(dec))   #转换成十六进制