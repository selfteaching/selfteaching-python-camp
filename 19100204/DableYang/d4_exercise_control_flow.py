# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={:<2}".format(i,j,i * j),end = " ")
    print(end="\n")
i = 1
while i<=9:
    j = 1
    if(i%2==1):
        while j<i+1:
            print("{}*{}={:<2}".format(i,j,i * j),end = " ")
            j += 1
        print (end="\n")
        i += 1
    else:
        i=i+1  