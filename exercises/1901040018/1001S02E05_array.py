l=list(range(10))
l.reverse()
l1=(str(i) for i in l)
l2=''.join(l1)
l3=l2[1:8]
l4=l3[::,-1]
print(l4)
