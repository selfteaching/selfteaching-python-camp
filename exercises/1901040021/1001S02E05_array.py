#创建数组a_list
a_list=[i for i in range(10)]
print(a_list)

#翻转数组a_list
a_list.sort(reverse=True)
print(a_list)

#将翻转之后的数组b_list拼接成a_str
b_list=[str(i) for i in a_list]
print(b_list)

a_str=''.join(b_list) #拼接
print(a_str)

c_str=a_str[3:9] #对string a_str 切边，取其第3到第8个字符
c_str.swapcase() #翻转string c_str

int(c_str) #convert string to int 

print(bin(int(c_str)))  #convert 10进制 to 2进制
print(oct(int(c_str)))  #convert 10进制 to 8进制
print(hex(int(c_str)))  #convert 10进制 to 16进制
