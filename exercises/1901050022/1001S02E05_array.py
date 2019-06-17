array=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array.reverse() #将数组翻转
print(array)

#翻转后的数组拼接成字符串
s = ''
for i in range(0,10):
    array[i]=str(array[i])
zifuchuan=s.join(array)
print(zifuchuan)

r1=zifuchuan[2:8] #第三到第八个字符
print(r1)
zhengshu=int(r1[::-1])#int类型
print(zhengshu)
print(bin(zhengshu))#二进制
print(oct(zhengshu))#八进制
print(hex(zhengshu))#十六进制