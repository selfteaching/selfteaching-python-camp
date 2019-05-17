list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
list1.reverse()#翻转数组
#print(list1)

list2 = []           #列表推广用方括号，阔起来
for i in list1 :     #注意冒号。一定得写
     i = str(i)      #str字符串的定义类型，有str的下一步就是想把数组或者字母弄成字符串类型
     list2.append(i) #将数组转化成字符串组 
#print(list2)
str1 = ''             #字符串一等于空格？？？？？？？这里面有两个str1，打印的时候是哪一个
str1 = str1.join(list2)#拼接成字符串，join是字符串的拼接函数，把空格当作拼接点
#print（str1)          #相当于把字符串都连在一块了
str2 = str1[2:8]      #用字符串切片的方式，取出第三到第八个字符.这里有一个bug.第一次输入为什么显示需要输入整型
#print(str2)           #字符串难道不能打印吗

str3 = int(str2)      #转化成int类型，整型？？？？？？？？？？这里面有两个str3，打印的时候是哪一个
#print(str3)

number1 = bin(str3)  #转化成二进制
number2 = oct(str3)  #转化成八进制
number3 = hex(str3)#进制数转换 
print(number1,number2,number3,sep='\n')