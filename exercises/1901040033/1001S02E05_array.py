array = [0,1,2,3,4,5,6,7,8,9] #定义arry
array.reverse()#将arry翻转
print(array)#打印arry


array1 = []#array1等于一个空的列表
for i in array:
    array1.append(str(i))#拼接成字符串
print(array1)#打印 array1
array2 = ''.join(array1)#拼接
print(array2)#打印array2

array3 = array2[2:8]#array3等于array2从第三个数字到第八个数字
print(array3)#打印array3

array4 = []#array4等于一个空的列表
for i in array3:
    array4.append(str(i))#拼接成字符串
array4.reverse()#将arry4翻转
print(array4)#打印 array4
array5 = ''.join(array4)#拼接
print(array5)#打印 array5

#将结果转换为int型
array6 =[]#array6等于一个空的列表
for i in array5:
    array6.append(int(i))#将arry5转换成整数
print(array6)#打印 array6

array7 = []
array8 = []
array9 = []
for i in array6:
    array7.append(bin(i))#转换成二进制
    array8.append(oct(i))#转换成八进制
    array9.append(hex(i))#转换成十六进制
print(array7,array8,array9)#打印
