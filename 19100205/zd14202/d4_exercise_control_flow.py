#九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(i) + "×" + str(j) + "=" + str(i*j),end = "") 
    print(" ")

#while循环乘法表
i = 1   
while i < 10:
     k = 1
     while k <= i:
         print('%d*%d=%2d   '% (i,k,i*k),end='') #end=‘’  表示不换行（系统默认输出完毕换行）
         k += 1
     print()
     i += 1

#删除偶数行
i=1
while i<=9:
    k=1
    while i% 2 !=0 and k < i+1:#while k <i+1 这是完整的乘法口诀表
        print("%d*%d=%-2d"%(i,k,i*k),end ="")
        k+=1
    print()
    i+= 1

