#for 循环打印乘法表
for a in range(1,10):
    for b in range(1 , a+1):   
        if(b == a):
            print(a," * ",b," = ",a * b)
        else:
            print(a," * ",b," = ",a * b,end = "     ")

#打印分隔符
print()
s = 'while循环控制输出奇数列表'
print(s.center(150,'*'))
print()

c = 1
d = 1
while (c < 10):
    while (d < 10):
        if (c % 2 != 0):
            if(c == d):
                print(c," * ",d," = ",c * d)
                d = 1
                c += 1
            else:
                print(c," * ",d," = ",c * d,end = "     ")
                d += 1
        else: 
            c += 1
            break

