Array = [x for x in range(1,10)]
#reverse the items of Array in place
Array.reverse()
#convert the array to string
def list_to_str(List):
    list_to_string = ''
    for num in List:
        list_to_string += str(num)
    return list_to_string
#slice the string
sliced_string = list_to_str(Array)[3:9]

#reverse the items of string in place
List = list(sliced_string)
List.reverse()
reversed_str = ''.join(List)

#convert string to int
str_to_int = int(reversed_str)

#convert to bin/oct/hex
int_to_bin = bin(str_to_int)
int_to_oct = oct(str_to_int)
int_to_hex = hex(str_to_int)

