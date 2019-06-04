list_1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_1.reverse()   #反转元素的位置
print(list_1)

#数组拼接为字符串
list_1=''.join(str(i) for i in list_1)  #list1=“”是不带空格的
print(list_1)

#切片的方式取出第三到第八个字符
list_2=list_1[2:8]         #空格也算字符
print(list_2)

#将获得字符串进行翻转
list_3=list_2[::-1]
print(list_3)

#将结果转换为INT类型
int_1=int(list_3)
print(int_1)

#分别转换为二进制，八进制，十六进制
print('转换成二进制为:',bin(int_1))
print('转换成八进制为:',oct(int_1))
print('转换成十六进制为:',hex(int_1))