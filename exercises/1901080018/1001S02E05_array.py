x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x2=x[::-1]
print(x2)
x3="".join(str(i) for i in x2)
print(x3)
x4=x3[3:9]
print(x4)
x5=x4[::-1]
print(x5)
x6=int(x5)
print(x6)
print(bin(x6))
print(oct(x6))
print(hex(x6))