'''
1.将数组[0,1,2,3,4,5,6,7,8,9]翻转
2.翻转后的数字拼接成字符串
3.用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
4.将获得的字符串进行翻转
5.将结果转为int类型
6.分别转换成二进制、八进制、十六进制
7.输出三种进制的结果
'''

#数组转为字符串
def array_to_str(array):
    array_str = ['']*len(array) #创建空的字符串列表
    for i in range(len(array)): #填补字符串列表
        array_str[i] = str(array[i])
    s = ''
    return s.join(array_str) #合并为一个字符串

#字符串翻转
def str_reverse(string):
    array_list=['']*len(string) #创建空的字符串列表
    for i in range(len(string)): #填补字符串列表
        array_list[i]=string[i]
    array_list.reverse() #翻转字符串列表
    s=''
    return s.join(array_list) #合并为一个字符串

array = [0,1,2,3,4,5,6,7,8,9]
array.reverse() #翻转数组
array_str = array_to_str(array) #数组转为字符串
array_str = array_str[2:8] #用字符串切片的方式取出第三到第八个字符
array_str = str_reverse(array_str) #字符串翻转
array_int = int(array_str) #将结果转为int类型
#分别转换成二进制、八进制、十六进制
#参考网页：http://www.runoob.com/python3/python3-conversion-binary-octal-hexadecimal.html
print('二进制数为：',bin(array_int))
print('八进制数为：',oct(array_int))
print('十六进制数为：',hex(array_int))
