print('九九乘法运算')
for i in range(1,10):
    for j in range(1,10):
        print(j,'×',i,'=',i*j, end="\t")
    print("")


print('九九乘法运算')
for a in range(1,10,2):
    for b in range(1,10,2):
        print(b,'×',a,'=',a*b, end="\t")
    print("")

print('九九乘法运算')
for c in range(1,10):
    for d in range(1,c+1):
        while c % 2 !=0:
            print(d,'×',c,'=',c*d, end="\t")
            if c == d:
                print("")
            break