i = 1
j = 1

while i <= 9:
        if(i % 2 == 0):
            j = 1
            i = i+1
        else :
            while(j <= i):
                    print(str(i) + "*" + str(j) + "=" + str(j*i) , end = "\t")
                    j = j+1
            else:
                    j = 1
                    i = i+1
                    print(end = "\n")
                    continue