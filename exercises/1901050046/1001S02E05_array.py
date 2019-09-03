list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list1.sort(reverse = True)
#print(list1)
str1 = ''
for i in list1:
        str1 = str1+str(i)
#print(str1)
str2= str1[2:8]#切片
str3 = str2[::-1]#字符串翻转
intNum = int(str3)
#print(intNum)
print(bin(intNum))
print(oct(intNum))
print(hex(intNum))
