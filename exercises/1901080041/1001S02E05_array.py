# 将数组[0,1,2,3,4,5,6,7,8,9]翻转
a_list = [0,1,2,3,4,5,6,7,8,9]
b_list = a_list [::-1]
print ('翻转列表:\n',b_list)

# 翻转后的数组拼接成字符串
Numberstr =''.join([str(i) for i in b_list])
print('拼接字符串:\n', Numberstr)

# 用字符串切⽚的⽅式取出第三到第⼋个字符(包含第三和第⼋个字符) 
slicestr = Numberstr[2:8]
print('切片字符:\n', slicestr)

# 将获得的字符串进⾏翻转
b_slicestr = slicestr[::-1]
print('翻转字符串:\n',b_slicestr)
    
# 将结果转换为int类型
intstr = int(b_slicestr)
print('转int类型：\n', intstr)

# 分别转换成⼆二进制，⼋八进制，⼗十六进制 
print('二二进制：\n', bin(intstr))
print('八八进制：\n', oct(intstr))
print ('十六进制：\n',hex(intstr))
