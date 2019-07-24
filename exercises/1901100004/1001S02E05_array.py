list = [0,1,2,3,4,5,6,7,8,9]
list.reverse()
print(list) 
list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
list3 = [str(i)for i in list2]
str1 = ''.join(list3)
print(str1)
str2 = str1[2:9]
print(str2)
str3 = str2[::-1]
print(str3)
num1 = int(str3)
two = bin(num1)
eight = oct(num1)
sixteen = hex(num1)
print(two)
print(eight)
print(sixteen)

