list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_list=list[::-1]
print(reversed_list)
joined_str=''.join(str(i) for i in reversed_list)
print(joined_str)
sliced_str=joined_str[2:8]
print(sliced_str)
reversed_list=sliced_str[::-1]
print(reversed_list)
int_value=int(reversed_list)
print(int_value)
print(bin(int_value))
print(oct(int_value))
print(hex(int_value))
