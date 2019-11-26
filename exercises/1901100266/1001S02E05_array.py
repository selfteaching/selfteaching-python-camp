sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sample_list.reverse()
print(sample_list)

joined_str = ''.join([str(i) for i in sample_list])
print(joined_str)#''表连接时，不需隔开字符；join()连接列表的元素

sliced_str = joined_str[2:8]
print(sliced_str)

reversed_str = sliced_str[::-1] #[::-1]是啥意思？-1是the last number，：是从头到尾的意思，：：是从翻转的意思？
print(reversed_str)

int_value = int(reversed_str) #转化为int类型，但是why？

print(int_value)

print(bin(int_value))
print(oct(int_value))
print(hex(int_value))