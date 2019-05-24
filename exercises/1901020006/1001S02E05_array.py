arr=[i for i in range(10)]
arr.sort(reverse=True)

str=''.join(str(i) for i in arr)

str1=str[3:9]

str2=str[::-1]

num=int(str2)
print('转换为:',num)     #输出成二进制,八进制,十六进制
print('\n二进制为:\n',bin(num))
print('\n八进制为:\n',oct(num))
print('\n十六进制为:\n',hex(num))    #明日重看