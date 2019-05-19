# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"*",i,"=",i*j,"\t",end='')
#     print("")

# 首先想到的去偶数行
# for i in range(1,10,2):
#     for j in range(1,i+1):
#         print(j,"*",i,"=",i*j,"\t",end='')
#     print("")

# 用while的去偶数行
for i in range(1,10,2):
    for j in range(1,i+1):
        while j<=9:
            break
        print(j,"*",i,"=",i*j,"\t",end='')
    print("")
 