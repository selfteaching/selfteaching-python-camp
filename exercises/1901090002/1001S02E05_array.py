list = [0,1,2,3,4,5,6,7,8,9]
list.reverse()
str_mine = ''
for num in list:
    str_mine += str(num)
new_str = str_mine[2:8]
str_reverse = new_str[::-1]
str_to_int = int(str_reverse)
two = bin(str_to_int)
eight = oct(str_to_int)
sixteen = hex(str_to_int)
print(two)
print(eight)
print(sixteen)