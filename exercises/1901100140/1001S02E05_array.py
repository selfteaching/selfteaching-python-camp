[0,1,2,3,4,5,6,7,8,9]
sample_list=[0,1,2,3,4,5,6,7,8,9]
reverse_list=sample_list[::-1]
print(reverse_list)

#将翻转后的数组拼接成字符
joined_str="".join(str(i) for i in reverse_list)
print(joined_str)

#用字符切片的方式取出第三到第八个字符
sliced_str=joined_str[2:8]
print(sliced_str)

#将获得的字符串进行反转
reverse_str=sliced_str[::-1]
print(reverse_str)

#将结果转换为int类型
int_value=int(reverse_str)
print(int_value)

#分别转换成二进制、八进制、十六进制
print(bin(int_value))
print(oct(int_value))
print(hex(int_value))

