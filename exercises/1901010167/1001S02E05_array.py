#将数组反转
list1=[0,1,2,3,4,5,6,7,8,9]
list1.reverse()
print(list1)
print('-------------------------------')
#将反转后的数组拼接成字符串
list2=[str(i) for i in list1]
print(list2)
string=''.join(list2)
print(string)
print('------------------------------')
#用字符串切片方式获取第三到第八个字符
s1=string[2:8]
print(s1)
print('------------------------------')
#将得到的字符串进行反转
s2=s1[::-1]
print(s2)
print('--------------------------------')
#将结果转换为int类型
numb=int(s2)
print(numb)
print('--------------------------------')
#将整数分别转换为二进制、八进制、十六进制
print(hex(numb))                #十六进制
print(oct(numb))                #八进制
print(bin(numb))                #二进制

