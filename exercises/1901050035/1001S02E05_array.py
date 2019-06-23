#Selflearning day5 homework partIII ,handling array!

s1=[0,1,2,3,4,5,6,7,8,9] #数值列表 

s1.reverse() #翻转列表元素的排列顺序
s2=s1
print(s2) 

s3=[]
for i in s2:
    s3.append(str(i)) #调用函数str()将非字符串值表示为字符串
print(s3)  

s4 = ''
s4=s4.join(s3) #将字符逐个加入s4，此时输出为'9876543210'
print(s4)

s5=s4[2:8] #切片从2开始到8结束‘2-7’
print(s5)

s6=list(s5)#列表
s6.reverse() #翻转列表元素的排列顺序
print(s6)

s7=[]
for i in s6:
    s7.append(int(i)) #将字符串转换为整数
print(s7)

s8=[]
s9=[]
s10=[]
for i in s7:
   s8.append(bin(i))  #将整数转换成2进制字符串
   s9.append(oct(i))  #将整数转换成8进制字符串
   s10.append(hex(i))  #将整数转换成16进制字符串

print(s8,s9,s10)

#【输出结果】
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
 ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
9876543210
765432
['2', '3', '4', '5', '6', '7']
[2, 3, 4, 5, 6, 7]
['0b10', '0b11', '0b100', '0b101', '0b110', '0b111'] ['0o2', '0o3', '0o4', '0o5', '0o6', '0o7'] ['0x2', '0x3', '0x4', '0x5', '0x6', '0x7']


    
 


