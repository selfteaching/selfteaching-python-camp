

num_array = [0,1,2,3,4,5,6,7,8,9]
new_array = sorted(num_array,reverse = True)

for i in new_array:
   new_array[9-i] = str(i)

str_array = ''.join(new_array)

#切片
str_array = str_array[2:8]
str_array = sorted(str_array)

#转整形
for i in str_array:
    str_array[int(i) - 2] = int(i)

#转2进制
for i in range(0,6):
    str_array[i] = bin(str_array[i])
print("**********************转2进制************************")
print(str_array)

#转8进制
for i in range(0,6):
    str_array[i] = oct(int(str_array[i],2))
print("*********************转8进制*************************")
print(str_array)

#转16进制
for i in range(0,6):
    str_array[i] = hex(int(str_array[i],8))
print("*********************转16进制*************************")
print(str_array)