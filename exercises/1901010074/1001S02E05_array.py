array =  [0,1,2,3,4,5,6,7,8,9]

array.reverse()

str = ''.join(str(i) for i in array)
num =int(str[2:8])
print(bin(num))
print(oct(num))
print(hex(num))