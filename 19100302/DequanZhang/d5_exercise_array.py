
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.reverse() #翻转数组
a = [str (x) for x in a]    #将翻转后的数组拼接成字符串
str1 = ''.join(a)
str2 = str1[2:8]   #用字符串切片的方式，取出第三到第八个字符（包含第三和第八个字符）
str3 = str2[::-1]    #将获得的字符串进行翻转
str4 = int(str3)      #将结果转换为int类型
print('二进制',bin(str4))   ##分别转化成二进制、八进制、十六进制
print('八进制',oct(str4))   #最后输出三种进制的结果
print('十六进制',hex(str4))


