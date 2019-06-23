data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    #创建数组
data.reverse()                           #将数组翻转
data_string = ''        
for i in data:
    data_string += str(i)
data_part = data_string[2:8]             #取出3-8个字符
data_part = data_part[::-1]              #字符翻转
data_part = int(data_part)               #转成int类型

print('二进制：', bin(data_part))         #打印二进制
print('八进制：', oct(data_part))         #打印八进制
print('十六进制:', hex(data_part))        #打印十六进制