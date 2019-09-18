list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list.reverse() #将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转
print(list)
list_str=''.join([str(x) for x in list]) #翻转后的数组拼接成字符串
print(list_str)
list_str[3:9] #用字符串切⽚的⽅式取出第三到第八个字符（包含第三和第八个字符）
print(list_str[3:9])
str1=list_str[3:9]
print(str1[::-1]) #将获得的字符串进行翻转
str2=str1[::-1]
int(str2) #将结果转换为 int 类型
print(int(str2))
int1=int(str2)
print(bin(int1)) #转换成二进制并输出结果
print(oct(int1)) #转换成八进制并输出结果
print(hex(int1)) #转换成十六进制并输出结果