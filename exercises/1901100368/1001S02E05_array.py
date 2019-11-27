array_test = [0,1,2,3,4,5,6,7,8,9]
array_test.reverse()#将数组翻转
str_test = '' #翻转后的数组拼接成字符串方法一
for i in range(0,10):
    array_test[i]=str(array_test[i])
string_test = str_test.join(array_test)
string_div =string_test[2:8] #用切片方式取出第三到第八个字符
int_test = int(string_div[::-1]) #将字符串进行反转，并转换为int类型
print(int_test)
print(bin(int_test),oct(int_test),hex(int_test))  #转换成二进制，八进制，十六进制