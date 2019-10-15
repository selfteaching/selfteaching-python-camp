for i in range(1,10):             # 输出9行
    for j in range(1,i+1):        # 输出与函数相等的列
        print(str(j)+"×"+str(i)+"="+str(i*j)+"\t",end='')
    print("")                     # 换行

for a in range(1,10):
    for b in range(1,a+1):
        while a % 2 != 0:
            print(str(b)+'×'+str(a)+'='+str(a*b)+'\t',end='')
            if a == b:
                print()
            break
