# 1st task : use function of "for...in" to build times table
print("Task 1:")
for a in range(1,10):
    for b in range (1,(a+1)):
        print(a,"*",b," = ", a*b,end='\t')
    print()

# 2nd task : use function of "while" to build times table with odd number only
print("Task 2-1:") # simply add '2' to get odd numbers
c = 1
while c <= 9:
    d = 1
    while d <= c:
        print(c,"*",d," = ",c*d,end="\t")
        d += 1
    c += 2
    print()    

print("Task 2-2:") # use condition to identify odd numbers
c = 1
while c <= 9:
    d = 1
    if(c%2==1):
        while d <= c:
            print(c,"*",d," = ",c*d, end='\t')
            d += 1
        print()
    else:
        d += 1
    c += 1