for i in range(1,10,1):
    for j in range(1,i+1,1):
        if(j < i):
            print(str(i) + "*" + str(j) + "=" + str(j*i) , end = "\t")
        else:
            print(str(i) + "*" + str(i) + "=" + str(j*i) , end = "\n") 
