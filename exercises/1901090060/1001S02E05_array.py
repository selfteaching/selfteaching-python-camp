#将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list1.reverse()
print('翻转数组为：\n{}'.format(list1))

#翻转后的数组拼接成字符串
list2 = [str(i) for i in list1]  #推导式创建的列表中的元素均为str
str1 = ''.join(list2)
print('\n翻转后的数组拼接成字符串：\n{}'.format(str1))

#用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
str2 = str1[2:8]
print('\n第三到第八个字符（包含第三和第八个字符）为:\n{}'.format(str2))

#将获得的字符串进行翻转
list3 = list(str2)   #字符串变为列表
list3.reverse()  #列表翻转
str3 = ''.join(list3)
print('\n获得的字符串进行翻转为:\n{}'.format(str3))

#将结果转换为 int 类型
str4 = int(str3)
print('\n结果转换为 int 类型:\n{str}\n类型：{type}\n'.format(str = str4,type = type(str4)))

#分别转换成二进制，八进制，十六进制，最后输出三种进制的结果
binary = bin(str4)
print('二进制为：{}'.format(binary))
octal = oct(str4)
print('八进制为:{}'.format(octal))
hexadecimal = hex(str4)
print('十六进制为:{}'.format(hexadecimal))