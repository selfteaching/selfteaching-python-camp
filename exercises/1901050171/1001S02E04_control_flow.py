for i in range(1,10):
    for j in range(1,10):
        if i<=9:
            print(f"{j}*{i}={i*j}",end="\t")
    print("")



for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end="\t")
    print("")
