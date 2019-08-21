# This part is to print multiplication table by using the for...in loop
print("The Multiplication Table")
for i in range(1,10):
    for j in range(1,i+1):

        print(i,'*',j,'=',i*j,end='\t')

        print(i,'*',j,'=',i*j,end='  ')

    print('')

print('')
# This part is to print multiplication table without even numbers by using the while loop
print('The Multiplication Table Without Even Number')
i=1;
while i<10 :
    if i%2!=0:
        j=1;
        while j<=i:
            if j%2!=0:

                print(i,'*',j,'=',i*j,end='\t')

                print(i,'*',j,'=',i*j,end='  ')

            j+=1
        print("")
    i+=1