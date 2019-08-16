#将数组[0,1,2,3,4,5,6,7,8,9]翻转,翻转后的数组拼接成字符串
a=[0,1,2,3,4,5,6,7,8,9]

a.reverse()
print(a)

a1=[str(i) for i in a]
print(a1)
a2=" ".join(a1)
print(a2)

#用字符串串切⽚片的⽅方式取出第三到第⼋八个字符(包含第三和第⼋八个字符)
a3=a[3:9]
print(a3)

#将获得的字符串串进⾏行行翻转
a4 = list(reversed(a3))
print(a4)

#将结果转换为int类型


#分别转换成⼆二进制，⼋八进制，⼗十六进制 8. 最后输出三种进制的结果"""

a6=[bin(i) for i in a4]
a7=[oct(i) for i in a4]
a8=[hex(i) for i in a4]
print(a6)
print(a7)
print(a8)