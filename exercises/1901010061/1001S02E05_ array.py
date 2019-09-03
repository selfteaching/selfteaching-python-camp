list=[0,1,2,3,4,5,6,7,8,9]
list.reverse()
print(list)

list1=[str(i) for i in list] #使用列表推导，将数值型转为字符串类型
str="".join(list1) #使用join()将列表拼接为字符串
print(str)

str1=str[2:8]
print(str1)

str2=str1[::-1] #将字符串倒转(reverse)，通过设置步长为负数：从右边第一个开始对整个字符串切片，实现翻转。
print(str2)

i=int(str2) #string 转 int : int (string). int转string :str(int)
print(i)

print(bin(i),oct(i),hex(i)) #print(bin(i).replace('0b',''),oct(i).replace('0o',''),hex(i).replace('0x',''))

