#用for...in 循环实现99乘法表
for i in range (1,10):
    for j in range (1,i+1):
        print("{}*{} = {:<5}".format(i,j,i*j),end = " ")
    print("")

#while循环
i = 0
j = 1
while (i < 9):
    i += 1
    if i%2 == 0:
         continue
    print()
    j = 1
    while (j <= i):
        result = int(i)*int(j)
        print(i,'*',j,'=',result,end='\t')
        j += 1