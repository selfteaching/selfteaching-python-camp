#1.翻转列表（也叫数组）

a_list=[0,1,2,3,4,5,6,7,8,9]
fanzhuan_list=a_list[::-1]
print('翻转列表==>',fanzhuan_list)   #此时是int类型元素

#2.

A=''.join([str(j)for j in fanzhuan_list])  #''符号表示元素间不用任何字符隔开
                                                #转换成str类型 的列表
print('翻转后的数组拼接成字符串==>',A)

#3.
b_str=A[2:8]
print('用字符串切片的方式取出第三到八个字符==>',b_str)

#4.
C=b_str[::-1]
print('切片字符串翻转==>',C)

#5.
E=int(C)

print('转为int类型==》',E)

print('转为 二进制==》',bin(E))
print('转为 八进制==》',oct(E))
print('转为 十六进制==》',hex(E))