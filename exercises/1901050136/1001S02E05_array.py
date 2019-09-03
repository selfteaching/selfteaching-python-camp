# this script is to implement
# reverse the list or the array, in python list is also called array
# 1 reverse the list
# method 1
list_sample = [0,1,2,3,4,5,6,7,8,9]
list_reverse = list_sample[::-1]
print("list_reverse",list_reverse)
# method 2
list_sample = [0,1,2,3,4,5,6,7,8,9]
list_sample.reverse()

# 2 translate the reverse list to string
# method 1
string = ''
for _i in list_reverse:
    string = string+(str(_i))
print("str",string)
# method 2
# list_sample = [0,1,2,3,4,5,6,7,8,9]
# list_reverse = list_sample[::-1]
for _i in range(len(list_reverse)):
    list_reverse[_i] = str(list_reverse[_i])
string = ''.join(list_reverse)
print("str2",string)

# 3 pick the 3rd to 8th char in the list
list_pick = string[2:8]
print("pick up the 3 to 8 slice in the string",list_pick)

# 4 reverse the picked string
# list_pick_reverse = list_pick.reverse() # string do not have the reverse() other than list
list_pick_reverse = list_pick[::-1]
print("reverse the picked list",list_pick_reverse)

# 5 integer the picked list
list_pick_reverse_int = int(list_pick_reverse)
print("integer the picked list",list_pick_reverse_int)

# 6 binary octonary Hexadecimal of the int value
list_pick_reverse_bin = bin(list_pick_reverse_int)
list_pick_reverse_oct = oct(list_pick_reverse_int)
list_pick_reverse_hex = hex(list_pick_reverse_int)
print("binary value is: {a}: ".format(a = list_pick_reverse_bin))
print("octonary value is: {b}: ".format(b = list_pick_reverse_oct))
print("Hexadecimal value is: {c}: ".format(c =list_pick_reverse_hex))

