array=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array.reverse()
array_string = ''
for x in array:
    array_string += str(x)
    
array_string = array_string[2:8]
array_string = array_string[::-1]
array_value = int(array_string)
print(bin(array_value))
print(oct(array_value))
print(hex(array_value))