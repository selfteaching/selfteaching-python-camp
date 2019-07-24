arr = [0,1,2,3,4,5,6,7,8,9]
arr1 = arr[::-1]
str1 = ''.join(map(str,arr))
str2 = str1[2:8]
str3 = str2[::-1]
num = int(str3)
print(num,"的二进制是  ",bin(num))
print(num,"的八进制是  ",oct(num))  
print(num,"的十六进制是",hex(num))  