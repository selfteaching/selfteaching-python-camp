arr1 = [1,2,3,4,5,6,7,8,9]
arr1.reverse()  
str1 = ''.join(map(str,arr1))   
str2 = str1[2:8]
str3 = str2[::-1]
str4 = int(str3)
print("最后结果为:")  
print(str4,"转换为二进制：",bin(str4))
print(str4,"转换为八进制：",oct(str4))
print(str4,"转换为十六进制：",hex(str4))