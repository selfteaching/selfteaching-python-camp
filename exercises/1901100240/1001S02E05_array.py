# This algorithm is just show couple feature of list and string
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

array.reverse()     # Reverse the list
str1 = ''.join(map(str,array))      # Transform the list to string

str1 = str1[2:8]        # Cut the string from the third to the eighth element
str1 = str1[::-1]       # Reverse the order
int1 = int(str1)        # Transfer to the type integer

print("The binary result is ",bin(int1))    # Transfer to binary system
print("The octonary result is ",oct(int1))      # Transfer to octonary system
print("The hexadecimal result is ",hex(int1))       # Transfer to hexadecimal system
