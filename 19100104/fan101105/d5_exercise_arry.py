a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = a[::-1]
a2 = ''.join(str(i) for i in a)
print(a2)
a3=a2[2:8] 
print(a3)
a4=int(a3[::-1])
print(a4)
print(bin(a4),oct(a4),hex(a4))