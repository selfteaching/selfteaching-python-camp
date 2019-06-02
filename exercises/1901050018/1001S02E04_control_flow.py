print('\njiu jiu cheng fa biao:',end='')	
for i in range(10):	
        for j in range(i):	
                print(i,end='')	
                print('*',end='')	
                print(j+1,end='')	
                print('=',end='')	
                print(i*(j+1),end='')	
                print('\t',end='')	
        print('\n')	
print('\nOmmitting even rows:\n')	
for i in range(10):	
        if i % 2 == 0:	
                pass	
        else:	
                for j in range(i):	
                        print(i,end='')	
                        print('*',end='')	
                        print(j+1,end='')	
                        print('=',end='')	
                        print(i*(j+1),end='')	
                        print('\t',end='')	
                print('\n') 