arr1=[0,1,2,3,4,5,6,7,8,9]
#将数组翻转
arr1.reverse()
print(' 将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转==>',arr1)
d = "".join(map(lambda x:str(x),arr1))
#str1=','.join(arr1)
#print('将翻转后的数组拼接成字符==》'，str1)
print('翻转后的数组拼接成字符串==>',d)
#⽤字符串切⽚的⽅式取出第三到第⼋个字符（包含第三和第⼋个字符
print('⽤字符串切⽚的⽅式取出第三到第⼋个字符（包含第三和第⼋个字符)==>',d[2:8])
# 将获得的字符串进⾏翻转
d1=d[2:8]
d2=d1[::-1]
print('将获得的字符串进行翻转==>',d2)
#将结果转换为 int 类型  
int_value=int(d2)
print('#将结果转换为 int 类型',int_value)
print('转为二进制==>',bin(int_value))
print('转为八进制==>',oct(int_value))
print('转为十六进制==>',hex(int_value))