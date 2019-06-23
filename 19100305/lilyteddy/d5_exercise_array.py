a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

a = a[::-1]
print(a)

str3 = ''
seq5 = []

for i in range(len(a)):
    seq5.append(str(a[i]))

b = str3.join(seq5)
print(b)

c=b[2:8]
print(c)

d=int(c)
print(d)

dbin=bin(d)
doct=oct(d)
dhex=hex(d)

print(dbin)
print(doct)
print(dhex)