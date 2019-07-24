a=[1,2,3,4,5,6,7,8,9]
a.reverse()
print(a)

b=[str(i)for i in a]
print(b)
c="".join(b)
print(c)

letter = c
letter= letter[2:-1:1]
print(letter)

d = list(letter)
d.reverse()
print(d)

e = "".join(d)
f = int(e)
print(bin(f))
print(oct(f))
print(hex(f))