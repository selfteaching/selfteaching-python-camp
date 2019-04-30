# 使用 for...in循环打印九九乘法表
for i in range(1, 10):  # i的范围从1到9  
    for j in range(1,i + 1):  # j的范围从1到i+1
        print(f'{i}*{j}={i*j}', end='\t')  # 输出表达式，并用制表符来空格
    print()  # 内循环结束后，换行。
print()

# 使用while循环打印九九乘法表，并用条件判断把偶数行去除掉
i = 1  # 给i赋初始值为1
while i <= 9 :  # i循环，从1到9
    if i % 2 != 0 :  # 判断i是否为偶数，若为偶数，执行i+1
        j = 1  # 给j赋初始值为1
        while j <= i :  #  j循环，从1到i
            print(f'{i}*{j}={i*j}', end='\t')  # 输出表达式，并用制表符来空格           
            j = j + 1  # 执行+1
        print()  # 内循环结束后，换行。   
    i = i + 1  # 执行+1
   
    
    

