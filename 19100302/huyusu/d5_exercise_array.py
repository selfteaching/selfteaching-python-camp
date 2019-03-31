
hu_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

hu_arr.reverse()

hu_str1 = ''.join(str(i) for i in hu_arr)

hu_str2 = hu_str1[3:9]

hu_str3 = hu_str2[::-1]

hu_int1 = int(hu_str3)



print('Converting to binary system: ',bin(hu_int1))
print('Converting to octonary number system: ',oct(hu_int1))
print('Converting to hexadecimal number system: ',hex(hu_int1))