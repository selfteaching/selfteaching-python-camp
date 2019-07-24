#1、创建一个名为d5_exercise_array.py的作业文件
#2、将数组[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]翻转
#3、翻转后的数组拼接成字符串
#4、用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
#5、将获得的字符串进行反转
#6、将结果转换为int类型
#7、分别转换成二进制，八进制，十六进制
#8、最后输出三种进制的结果

shuzu=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuzu.reverse() #将数组翻转
print(shuzu)

#翻转后的数组拼接成字符串
s = ''
for i in range(0,10):
    shuzu[i]=str(shuzu[i])
zifuchuan=s.join(shuzu)
print(zifuchuan)

r1=zifuchuan[2:8] #用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
print(r1)
zhengshu=int(r1[::-1])#将获得的字符串进行反转和将结果转换为int类型
print(zhengshu)
print(bin(zhengshu))#转换成二进制并输出
print(oct(zhengshu))#转换成八进制并输出
print(hex(zhengshu))#转换成十六进制并输出