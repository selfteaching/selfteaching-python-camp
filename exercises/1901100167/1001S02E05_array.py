set1= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
set1.reverse()
print (set1)
strset=(''.join('%s'%id for id in set1))
print (strset)
restrset=strset[2:8]
a=restrset[::-1]
print(a)
b=int(a)
print(b)
print(bin(b))
print(oct(b))
print(hex(b))
