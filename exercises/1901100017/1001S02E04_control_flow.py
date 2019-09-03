""" control flow
print out 9*9 multiply form """

number = 0
i = 0

for number in range(1,10):
    for i in range(1,number+1):
        print(number,"*",i,"=",(number*i),end='\t')
    print ('\n')

for number in range(1,10):
    for i in range(1,number+1):
        if number % 2 != 0:
            print(number,"*",i,"=",(number*i),end='\t')
        else:
            print ('\n')
            break
print('\n')
number = 1
while number < 10:
    if number % 2 != 0:
        for i in range(1,number+1):
            print(number,"*",i,"=",(number*i),end='\t')
    number = number + 1
    print('\n')
else:
    number = number + 1