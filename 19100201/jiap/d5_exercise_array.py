array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(type(array))

rev_array = list(reversed(array))
print(rev_array)

string = ""
for i in rev_array:
	string = string + str(i)
print(string)

str_three = string[2:9]
print(str_three)

rev_three = str_three[::-1]
print(rev_three)

int_three = int(rev_three)
print(int_three)

print(bin(int_three))
print(oct(int_three))
print(hex(int_three))