list_1 = [i for i in range(0,10)]
list_1.reverse()
print(list_1)
list_2 = [str(i) for i in list_1]
string_2 = ''.join(list_2)
print(string_2)
string_2 = string_2[3:9]
print(string_2)
string_3 = string_2[::-1]
print(string_3)
num = int(string_3)
print(num,type(num))
print('二进制:',bin(num))
print('八进制:',oct(num))
print('十六进制',hex(num))