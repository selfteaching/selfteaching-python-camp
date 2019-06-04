for a in range(1,10):
    for b in range(1,a+1):
        c = a * b 
        if a > b:
            print ("{}*{}={}".format(a, b, c), end="\t")
        if a == b:
            print ("{}*{}={}".format(a, b, c))
for a in range(1,10,2):
    for b in range(1,a+1):
        c = a * b 
        if a > b:
            print ("{}*{}={}".format(a, b, c), end="\t")
        if a == b:
            print ("{}*{}={}".format(a, b, c))
for a in range(1,10):
    for b in range(1,a+1):
        c = a * b 
        while int(a/2) != int((a+1)/2):
            if a > b:
                print ("{}*{}={}".format(a, b, c), end="\t")
            if a == b:
                print ("{}*{}={}".format(a, b, c))
            break
