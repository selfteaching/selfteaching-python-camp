a = [0,1,2,3,4,5,6,7,8,9]
print(list(reversed(a)))
#print输出 a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


a1 = ''.join(str(i) for i in a)
print(a1)
#print输出 a1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

a2 = a1[3:9]
print(a2)
#print输出 a2 = ['3', '4', '5', '6', '7', '8']

a3 = list(reversed(a2))
print(a3)
#print输出 a3 = ['8', '7', '6', '5', '4', '3']

a3 = map(eval,a3)
a4 = list(a3)
print(a4)

a5 = int(a2)
print(a5)
print(bin(a5))
print(oct(a5))
print(hex(a5))
