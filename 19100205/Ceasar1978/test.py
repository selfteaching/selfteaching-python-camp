
seq4 = [1, 2, 3]
seq5 = []
for i in range(len(seq4)):
    seq5.append(str(seq4[i]))
s6 = ''.join(seq5)
print (s6)
s7 = ''.join(str(i) for i in seq5)
print (s7)
