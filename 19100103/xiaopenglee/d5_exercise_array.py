array=[0,1,2,3,4,5,6,7,8,9] #输入数组
string=''                   #初始化字符串
array=sorted(array,reverse=True)    #翻转字符串
for i in range(0,len(array)):
    string=string+str(array[i]) #拼接字符串
string=string[2:8]              #切片取出元素
string=string[::-1]             #字符串翻转
string=int(string)              #将字符串转为整数
print(bin(string),'\n',oct(string),'\n',hex(string))    #二进制、八进制、十六进制 分别为bin\oct\hex