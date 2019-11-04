for a in range(1,10):
    for b in range (1,a+1):
        print(a,'*',b,'=',a*b,end='\t')
    print()



for a in range(1,10):
    if a%2==0:
        continue
    if a%2!=0:
        for b in range (1,a+1):
            print(a,'*',b,'=',a*b,end='\t')
    print()