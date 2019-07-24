for a in range(1, 10):
    for b in range(1, a+1):
        if a == b :
            print(a,'*',b,'=',a*b)
            break
        else:
            print(a,'*',b,'=',a*b,end='\t')
print('\n')

for a in range(1, 10):
    for b in range(1, a+1):
        while a % 2 == 1 :
            if a == b :
                print(a,'*',b,'=',a*b)
                break
            else:
                print(a,'*',b,'=',a*b,end='\t')
                break
print('\n')