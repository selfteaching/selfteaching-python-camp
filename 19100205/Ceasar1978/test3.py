def multiply(x,y):return x*y
i = 1
while i < 10:
    j = 1
    while i % 2 != 0 and j < i+1:
        print(j,'*',i,'=',multiply(j,i),end = '\t')
        j = j + 1
    print('')
    i = i + 1
    