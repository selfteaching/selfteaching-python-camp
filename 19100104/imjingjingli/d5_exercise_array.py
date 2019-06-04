nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums.reverse()     #翻转列表元素的排列顺序
# print(nums)

nums_str = ''      #创建空的字符串变量nums_str
for i in nums:     #依次从列表nums种拿出元素进行循环，此时nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    nums_str += str(i)  #调用函数str()将非字符串值表示为字符串，将字符逐个加入变量nums_str，此时输出为9876543210
# print(nums_str)

nums_3_8 = nums_str[2:8]  #切片从0开始
# print(nums_3_8)

nums_3_8_reverse = nums_3_8[::-1]  #从后往前切片
# print(nums_3_8_reverse)

num_int = int(nums_3_8_reverse)  #将字符转换为整数
# print(num_int)

num_2 = bin(num_int)  #返回整数的二进制
print(num_2)

num_8 = oct(num_int)  #将整数转换成8进制字符串
print(num_8)  

num_16 = hex(num_int)  #将十进制的整数转换成十六进制
print(num_16)