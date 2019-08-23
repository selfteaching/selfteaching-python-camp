# Print multiplication table by using the for...in loop
print("The Multiplication Table")

for i in range(1,10):       # The row start from 1 to 9
    for j in range(1,i+1):      # The column start from 1 to i
        print(i,'*',j,'=',i*j,end='\t')     # \t to make double blank
    print('')       # Start a new line for each row i

for i in range(1,10):
    for j in range(1,i+1):

        print(i,'*',j,'=',i*j,end='\t')

        print(i,'*',j,'=',i*j,end='  ')

    print('')


print('')


# Print multiplication table without even numbers by using the while loop
print('The Multiplication Table Without Even Number')

i=1     # The row start from 1
while i <= 9 :      # Loop the row from 1 to 9
    if i%2 != 0:        # Filter the even row
        j = 1       # The column start from 1
        while j <= i:       # Loop the column from 1 to i
            print(i,'*',j,'=',i*j,end='\t')     # \t to make double blank
            j += 1
        print("")       # Start a new line for each odd row

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