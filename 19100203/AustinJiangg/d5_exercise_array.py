list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list1.reverse()#翻转数组
#print(list1)

list2 = []
for i in list1:
    i = str(i)
    list2.append(i)#将数组转化成字符串组
    
str1 = ''
str1 = str1.join(list2)#拼接成字符串

str2 = str1[2:8]#取出第三到第八个字符

list3 = list(str2)
list3 = list3.reverse
str3 = str(list3)#翻转

str3 = int(str2)#转化成int类型

#print(str3)
number1 = bin(str3)
number2 = oct(str3)
number3 = hex(str3)#进制数转换

print(number1,number2,number3,sep='\n')