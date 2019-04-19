
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1.将数组翻转
arr.reverse()

#2.拼接为字符串
str1=''.join(map(str,arr))
'''
map(function, iterable, ...)
返回的是map型，
参数function: 传的是一个函数名，可以是Python内置的，也可以是自定义的
参数iterable 传的是一个可以迭代的对象，例如列表，元祖，字符串
功能：将iterable中的每一元素执行一遍function
'''

#方法二
str1 = ''.join(str(i) for i in arr)
#join不能直接拼接数字型数组，需要用到for in 函数

#3.用字符串切片的方式取出第三个到第八个字符
str2 = str1[2:8]

#4、将获得的字符串进行反转
str3=str2[::-1]

#5、将结果转为int型

int1 = int(str3)

#6.分别转换成二进制，八进制，十六进制
print('十进制整数为：',int1)
print('转换成二进制为:',bin(int1))
print('转换成八进制：',oct(int1))
print('转换成十六进制为：',hex(int1))
