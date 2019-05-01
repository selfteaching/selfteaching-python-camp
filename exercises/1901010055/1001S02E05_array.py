array=[0,1,2,3,4,5,6,7,8,9]
array.reverse()
print(array)
array1=[]
for i in array:
    array1.append(str(i))#字符串
print(array1)
array2 = ''.join(array1)#拼接
print(array2)
array3 = array2[2:8]#取值
print(array3)
array4 = []
for i in array3:
    array4.append(str(i))#字符串
array4.reverse()#翻转
print(array4)
array5 = ''.join(array4)#拼接
print(array5)
array6 =[]
for i in array5:
    array6.append(int(i))#转换成整数
print(array6)

array7 = []
array8 = []
array9 = []
for i in array6:
    array7.append(bin(i))#转换成二进制
    array8.append(oct(i))#转换成八进制
    array9.append(hex(i))#转换成十六进制
print(array7,array8,array9)