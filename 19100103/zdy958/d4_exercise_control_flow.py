for a in range(1,10):#Part.1.E.3.controlflow.ipynb
    for b in range(1,a+1):
        c = a * b 
        if a > b:
            print ("{}*{}={}".format(a, b, c), end="\t")#制表符
        if a == b:
            print ("{}*{}={}".format(a, b, c))
for a in range(1,10,2):#1开始，2为等差数列
    for b in range(1,a+1):
        c = a * b 
        if a > b:
            print ("{}*{}={}".format(a, b, c), end="\t")
        if a == b:
            print ("{}*{}={}".format(a, b, c))
i = 1
while i<=9:
    j = 1
    while j<=i:
        print("{}*{}={:<2}".format(i,j,i * j),end="\t")
        j += 1
    i += 1
    print("")
i = 1
while i<=9:
    j = 1
    while j<=i:
        print("{}*{}={:<2}".format(i,j,i * j),end="\t")
        j += 1#第二列的数值差值为1
    i += 2#第一列的数差值为2
    print("")    