l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l.reverse()
print("将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转")
print(l)    #如果在这里面直接进行list转str处理的话，会出现错误。
print("将翻转后的列表拼接成字符串")
s = "".join(map(str,l))  #由于list中都是int，需要采用map函数将list中的每个int转换成str格式，才可以拼接
print(s)
print("用字符串切片方式取出第三到第八个字符（包含第三和第八个字符）")
s1 = s [2:8]
print(s1)
print("将获得的字符串进行翻转")
s2 = s1[::-1]   #以步长为1反向读取字符串
print(s2)
print("将字符串输出结果转换为int类型")
i = int(s2)
print(i)
print("将整数分别转化为二进制、八进制、十六进制") #属于数字运算
print(bin(i))
print(oct(i))
print(hex(i))
