#numbers=[1,2,3,4,5,6,7,8,9]
#number=[1,2,3,4,5,6,7,8,9]
for i in range(1,10):
    print('\n')
    for j in range(1,i+1):
       print(i,'*',j,'=',i*j)



c = 1
while c <= 9:
    b = 1
    while b <= c:
        print("%d*%d=%-2d"%(c,b,c*b),end = ' ')
        b += 1
    print()
    c += 2