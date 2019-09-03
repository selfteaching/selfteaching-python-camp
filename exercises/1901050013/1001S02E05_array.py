array = [0,1,2,3,4,5,6,7,8,9] 
array.reverse()
str = ''.join(str(i) for i in array)
str1 = str[2:8]
str2 = str1[::-1]
int = int(str2)
bin = bin(int)
oct = oct(int)
hex = hex(int)
print(bin)
print(oct)
print(hex)