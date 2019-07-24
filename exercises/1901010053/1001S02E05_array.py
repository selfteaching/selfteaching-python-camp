
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1.将数组翻转
arr.reverse()

#2.拼接为字符串

#方法一：
str1=''.join(map(str,arr))
#map(function, iterable, …)
#返回的是map型，（ps：python2中返回的是list型可以直接显示，但在python3中是 * map型无法直接显示 *）
#参数function： 传的是一个函数名，可以是python内置的，也可以是自定义的。
#参数iterable ：传的是一个可以迭代的对象，例如列表，元组，字符串这样的
#功能：将iterable中的每一个元素执行一遍function

#方法二：
str1 = ''.join(str(i) for i in arr)
#join不能直接拼接数字型数组，需要用到for in函数。 * 但我不理解这样的语句书写方式 str(i) for i in arr *

#3.用字符串切片的方式取出第三个到第八个字符（包含第三和第八个字符）
str2 = str1[2:8]
#格式： [start:end:step]
#• [:] 提取从开头（默认位置0）到结尾（默认位置-1）的整个字符串
#• [start:] 从start 提取到结尾
#• [:end] 从开头提取到end - 1
#• [start:end] 从start 提取到end - 1
#• [start:end:step] 从start 提取到end - 1，每step 个字符提取一个

# 4.将获得的字符串进行反转
str3=str2[::-1]

# 5.将结果转为int型
int1 = int(str3)

# 6.分别转换成二进制，八进制，十六进制
print('十进制整数为: ',int1)
print('转换成二进制为: ',bin(int1))
print('转换成八进制为: ',oct(int1))
print('转换成十六进制为: ',hex(int1))


