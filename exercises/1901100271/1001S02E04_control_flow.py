for i in range (1,10):
    for j in range (1,10):
        print (i,"*",j, "=", i*j, end='\t')
        if i == j:
            print ('\n')
            i = i + 1            
            break #break语句在这里是跳出for j的循环

            break

        else:
            j = j + 1
pass
print ("next work\n")

i = 1
while (i < 10):
    j = 1

    print (i,"*",j, "=", i*j, end='\t')
    while (j < i):
        j += 1
        print (i,"*",j, "=", i*j, end='\t')

    if i % 2 == 0:
        break
    else:
        print (i,"*",j, "=", i*j, end='\t')
        while (j < i):
            j += 1
            print (i,"*",j, "=", i*j, end='\t')

    print ('\n')
    i += 2

