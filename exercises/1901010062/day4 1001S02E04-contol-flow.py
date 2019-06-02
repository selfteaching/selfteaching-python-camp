for i in range(1,10):
    for x in range(1,i+1):
        print('{}*{}={}\t'.format(x,i,i*x),end='')
    print()
print("") 


for i in range(1,10):
    for n in range(1,10):
        if n<=i:
            while n*i%2!=0:
                print(str(i),"*",n,"=",i*n,end='\t')
                break
    print("")