x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(reversed(x)))
n="".join(str (i) for i in x )
print(n)
m=n[3:9]
print(list(reversed(m)))
y="".join(str(j)for j in m)
print(y)
w=int(y)
print(bin(w))
print(oct(w))
print(hex(w))