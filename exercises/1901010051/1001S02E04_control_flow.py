#使用for......in循环打印九九乘法口诀表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j," ",end="")
    print("")


#使用while循环打印九九乘法表并用条件判断把偶数行去除掉
i = 1
while i < 10 :
    if i % 2 == 0 :
        i += 1
    continue 
    j = 1
    while j < i+j:
        print(i,"*",j,"=",i*j," ",end="")
        j += 1
    print("",end="\n")
    i += 1
