array = [0,1,2,3,4,5,6,7,8,9]
#翻转字符串
print(list(reversed(array)))
#拼接字符串
join_array = (''.join(list(map(str,array))))
print(join_array)

#截取第3到第8
slice_array = join_array[2:8]
print(slice_array)
#再翻转
reverve_str = slice_array[::-1]
print(reverve_str,type(reverve_str))
#convert to int
int_str = int(reverve_str)
print(int_str,type(int_str))
#print in brinary
print(bin(int_str))
#print octonary
print(oct(int_str))
#print hexadecimal
print(hex(int_str))