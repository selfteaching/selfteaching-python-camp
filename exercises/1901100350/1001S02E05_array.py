1#对列表翻转
a_list = [0,1,2,3,4,5,6,7,8,9]
reversed_list = (a_list[::-1])
print("list",reversed_list )

2#翻转列表拼接成字符串
join_str = ''.join([str(i) for i in reversed_list])
print('list',join_str)

3#用字符串切片的方式取出第三到第八个字符（包括八）
sliced_str = join_str[2:8]
print('list',sliced_str)

4#将获得的字符串翻转
reversed_str =sliced_str[::-1]
print('list',reversed_str)

5#将结果转换为int
int_value = int(reversed_str)
print('int',int_value)

6#转换为2进制
print('int',bin(int_value))

7#转换为8进制
print('int',oct(int_value))

8#转换为16进制
print('int',hex(int_value))