list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list. reverse()                       
print("翻转:",list) 

list_str = "".join((str(i) for i in list))   
print("字符串:",list_str)


jiequ_str = list_str[2:8]   
print("取字符 ",jiequ_str)

fz_str = jiequ_str[::-1]
print("翻转 :",fz_str)


m = int(fz_str)
print("int 类型:",m)

print("二进制:",bin(m))
print("八进制:",oct(m))
print("十六进制:",hex(m))
