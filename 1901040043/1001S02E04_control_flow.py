
for i in range(10):       #打印九九乘法表
    s=''
    for j in range(1,i+1):
        s+=str(j)+'*'+str(i)+'='+str(j*i)+'\t'
    print(s)




f=1       #九九乘法表去偶数行
while f<=9:
    if f%2!=0:
        h=1
        while h<f+1:
            print(f,"*",h,'=',f*h,sep='',end='\t')
            h+=1
        print()
    f+=1




f=1       #九九乘法表去奇数行
while f<=9:
    if f%2==0:
        h=1
        while h<f+1:
            print(f,"*",h,'=',f*h,sep='',end='\t')
            h+=1
        print()
    f+=1

for i in range(10):#打印1到9同因数乘法表
    s=''
    for j in range(1,i+1):
        s=str(j)+'*'+str(i)+'='+str(j*i)+'\t'
    print(s)
