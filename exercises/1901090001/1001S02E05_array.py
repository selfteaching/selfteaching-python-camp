list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
list2 = list1.reverse()
str = ''.join(str(i) for i in list1)
str1 = str[2:8]
str2 = str[::-1]
int = int(str2)

print(bin(int))
print(oct(int))
print(hex(int))