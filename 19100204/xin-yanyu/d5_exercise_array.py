# 第五天作业3
#  2019年3月25日
# 数组操作，进制转换 
# 1．创业一个名为d5_exercise_array. Py的作业文件 
# 2.将数组[0，1，2，3，4，5，6，7，8，9]翻转 
# 3.翻转后的数组拼接成字符串 
# 4.用字符串切片的方式取出第三到第八个字符(包含第三和第八个字符) 
# 5.将获得的字符串进行翻转 
# 6.将结果转换为int类型 
# 7.分别转换成二进制，八进制，十六进制 
# 8.最后输出三种进制的结果

num_arry=[0,1,2,3,4,5,6,7,8,9]


# 2.将数组[0，1，2，3，4，5，6，7，8，9]翻转 
n = len(num_arry)
n1=int(n/2)
# 数组前后交换
for i in range( n1 ):
	num_arry[i],num_arry[n - i - 1]=num_arry[n - i - 1],num_arry[i]
print ('arry row = ', num_arry)

# 3.翻转后的数组拼接成字符串 
num_chr=''
for i in range( n ):
	num_chr=num_chr + str(num_arry[i])
print('chr = ', num_chr)

# 4.用字符串切片的方式取出第三到第八个字符(包含第三和第八个字符) 

num_chr_cut=num_chr[2:8]
print('3-8 = ', num_chr_cut)

# 5.将获得的字符串进行翻转 
num_chr_cut_rol=num_chr_cut[::-1]
print('chr rol = ', num_chr_cut_rol)

# 6.将结果转换为int类型 
num_chr_cut_rol_int=int(num_chr_cut_rol)
print('chr->chr =',num_chr_cut_rol_int)

# 7.分别转换成二进制，八进制，十六进制 
nun_bin=bin(num_chr_cut_rol_int)
num_oct=oct(num_chr_cut_rol_int)  
num_hex=hex(num_chr_cut_rol_int)  

# 8.最后输出三种进制的结果
print('bin = ', nun_bin)
print('oct = ', num_oct)  
print('num = ', num_hex)  

# 6.将结果转换为int类型 
print('2->10 = ', int(nun_bin,base=2))
print('8->10 = ', int(num_oct,base=8))  
print('16->10 = ', int(num_hex,base=16))  
