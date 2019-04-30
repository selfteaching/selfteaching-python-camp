#将数组[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转
array = [0,1,2,3,4,5,6,7,8,9]
array.reverse()
print(array)

#翻转后的数组拼接成字符串
array1 = []
for i in array:
    array1.append(str(i))
print(array1)
array2 = ''.join(array1)
print(array2)

#用字符切片取出第三到第八个字符（包含第三和第八个字符）
array3 = array2[2:8]
print(array3)

#将获得的字符串进行翻转
array4 = []
for i in array3:
    array4.append(str(i))
array4.reverse()
print(array4)
array5 = ''.join(array4)
print(array5)

#将结果转换为int型
array6 =[]
for i in array5:
    array6.append(int(i))
print(array6)

#将获得的结果转换为二进制、八进制、十六进制
array7 = []
array8 = []
array9 = []
for i in array6:
    array7.append(bin(i))
    array8.append(oct(i))
    array9.append(hex(i))
print(array7,array8,array9)
