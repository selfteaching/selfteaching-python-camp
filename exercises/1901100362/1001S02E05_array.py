arr = [0,1,2,3,4,5,6,7,8,9]
#翻转arr数组
arr.reverse()

#将数组元素拼接成字符串
l1 = [str(a) for a in arr]
s1 = ''.join(l1)
print(s1)

#对字符串切片，取出第三到第八个字符
s2 = s1[2:9]
print(s2)
#对字符串进行翻转
s3 = s2[::-1]
print(s3)
#转换成十进制
in1 = int(s3)
#转换成8禁制
oct1 = oct(in1)
#转换成16进制
hex1 = hex(in1)
print(f'{oct1} \n{hex1}')

