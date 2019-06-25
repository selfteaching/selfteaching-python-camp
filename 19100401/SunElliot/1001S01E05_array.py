# Array process


data=[0,1,2,3,4,5,6,7,8,9]

data.reverse()

data_string=''
for i in data:
        data_string+=str(i)

data_part= data_string[2:8]  #取出第3-8个字符

data_part=data_part[::-1]  #字符反转

data_part=int(data_part)

print("十进制数为：", data_part)
print("转换为二进制为：", bin(data_part))
print("转换为八进制为：", oct(data_part))
print("转换为十六进制为：", hex(data_part))



