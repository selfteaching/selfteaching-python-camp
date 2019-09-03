# for x in y，这是个循环体
# 执行流程：x依次表示y中的一个元素，遍历完所有元素循环结束

print("1. 使⽤ for...in 循环打印九九乘法表，输出：")
print()
for i in range(1, 10):
# range(1, 10)函数表示1到9中的任意一个整数，不含10

    for j in range(1, i+1):
    # range(1, i+1)函数表示1到i+1中的任意一个整数，不含i+1

        print((i),"*",(j),"=",(i*j),end='  ')
        # 强调：(i)和"i"的含义不同，前者表示输出i所代表的数值，后者仍然输出i这个字母
        # end="  "表示不换行，以空格结尾
    
    print()
    # 这个表示换行

print("2. 使⽤while循环打印九九乘法表：")
i=1
while i<=9:
    j=1
    while j<=i:
        print(i,"x",j,"=",i*j,end='  ')
        j +=1
    print()
    i +=1
    
    
print("3. 使⽤while循环打印九九乘法表并用条件判断把偶数行去除掉,输出：")
i=1
while i<=9:
    if i % 2 == 0:
        print()
    else:
        for j in range(1,i+1):
            print(i,"x",j,"=",i*j,end='  ')
    i +=1


            
       
       
       
