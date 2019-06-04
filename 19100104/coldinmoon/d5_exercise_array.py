#1.将数组[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转
#2.翻转后的数组拼接成字符串
#3.用字符串切片的方式取出第三到第八的字符（包括第三和第八个字符）
#4.将获得的字符串反转
#5.将结果转换为int类型
#6.分别转换为二进制、八进制、十六进制
#7.输出三种进制的结果
#Date:3/22/2019

#将数组拼接成字符串
def array_to_str(array):
    array_str=['']*len(array)   #新建空字符串
    for i in range(len(array)): 
        array_str[i]=str(array[i])  #填充新字符串
    x=''
    return x.join(array_str)    #导出

#将字符串反转
def str_reverse(string):
    str_list=['']*len(string) #新建空字符串
    for i in range(len(string)):
        str_list[i]=string[i]    #填充新字符串
    str_list.reverse()  #翻转
    x=''
    return x.join(str_list) #导出

array=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array.reverse() #数列翻转
array_str=array_to_str(array) #数组拼接为字符串
array_str=array_str[2:8]    #切片
array_str=str_reverse(array_str)    #翻转字符串
str_array=int(array_str)    #转换为int
#分别转化为二进制、十进制、十六进制，并打印
print('最终，二进制数列为',bin(str_array))
print('最终，十进制数列为',oct(str_array))
print('最终，十六进制数列为',hex(str_array))




