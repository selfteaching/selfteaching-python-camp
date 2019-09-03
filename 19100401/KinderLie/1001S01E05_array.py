array=[0,1,2,3,4,5,6,7,8,9]

# 翻转
array.reverse() 
print(array)

# 拼接成字符串
c = [9,8,7,6,5,4,3,2,1,0]
array = [str(i) for i in array]
array = ''.join(array)
print(array)

# 取出第三到第八个字符（包含第三到第八个字符）")
array = array[2:8]
print(array)

# 翻转
array = array[::-1]
print(array)

# 转换为int类型
array = int(array)
print(array)

# 分别转换为二、八、十六进制
two = bin(array)
eight = oct(array)
sixteen = hex(array)

# 分别输出三种结果
print(two)
print(eight)
print(sixteen)