list1 = [0,1,2,3,4,5,6,7,8,9]
list1.reverse()
list2 = [str(i) for i in list1]
str1 = ''.join(list2)
str2 = str1[2:8]
str3 = str2[::-1]
num1 = int(str3)
print(bin(num1))
print(oct(num1))
print(hex(num1))