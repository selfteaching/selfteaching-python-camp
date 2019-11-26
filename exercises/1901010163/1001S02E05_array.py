array = [i for i in range(10)]
array.reverse()

array_str = [str(num) for num in array]
string = ''.join(array_str)
# print(string)

slice3_8 = string[2:8]
# print(slice3_8)

string_2 = ''.join(sorted(slice3_8))
# print(string_2)

integer = int(string_2)

bin_integer = bin(integer)
oct_integer = oct(integer)
hex_integer = hex(integer)

print(f'bin: {bin_integer}\noct: {oct_integer}\nhex: {hex_integer}')
