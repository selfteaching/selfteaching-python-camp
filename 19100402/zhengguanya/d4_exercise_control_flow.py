for i in range(1, 10):
    for j in range(1, i+1):
        print(i,'x',j,'=',i*j,' ',end='')

    print()

for i in range(1, 10):
    for j in range(1, i+1):

        while i==2 or i==4 or i==6 or i==8:
            
            break
        else:
            print(i,'x',j,'=',i*j,' ',end='')
    print()