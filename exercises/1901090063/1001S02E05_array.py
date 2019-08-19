
#创建数组并翻转
data=[x for x in range(10)]
data.reverse()

#将数组拼接成字符串
sr=str(data[0])
for i in range(1,10):
    sr=sr+str(data[i])

#取出第3到第8个字符
data1=sr[2:8]

#对字符进行翻转并转换成int类型
data2=int(data1[::-1])

#将结果分别转换成二进制、八进制和十六进制并输出
da1=bin(data2)
da2=oct(data2)
da3=hex(data2)
print(f'{data2} 转换为：\n二进制:{da1}\n八进制:{da2}\n十六进制:{da3}')