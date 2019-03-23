'''
1.将数组[0,1,2,3,4,5,6,7,8,9]翻转
2.翻转后的数字拼接成字符串
3.用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
4.将获得的字符串进行翻转
5.将结果转为int类型
6.分别转换成二进制、八进制、十六进制
7.输出三种进制的结果
'''


array=[0,1,2,3,4,5,6,7,8,9]
array.reverse() #将数组翻转
print(array)

s = ''      #翻转后的数组拼接成字符串方法一
for i in range(0,10):  
    array[i]=str(array[i])
zifucuan=s.join(array)
print(zifucuan)


r1=zifucuan[2:8]  #用切片方式取出第三到第八个字符
print(r1)
zh=int(r1[::-1])  #将字符串进行反转，并转换为int类型
print(zh)
print(bin(zh),oct(zh),hex(zh)) #转换成二进制、八进制、十六进制