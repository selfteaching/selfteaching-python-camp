a = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
a1 = list(reversed(a))
print(a1)

str = ''.join(str(i) for i in a1)
print(str)

a2 = str[2:8]
print(a2)

result = a2[::-1]
print(result)

int(result)
print(int(result))

dec = int(result)
print(bin(dec))
print(oct(dec))
print(hex(dec))