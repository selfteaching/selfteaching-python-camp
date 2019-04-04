#  控制流程学习程序
# 第四天 2019.4.4
# 1 ：用 for……in ……完成九九表打印

for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={}".format(i,j,i*j),end = " ")
    print()

# 2 ：用while打印九九表，并用条件判断把偶数行除掉
i = 1
while i <10:
    j = 1
    while j<=i:
        if i%2 == 0:
            break
        print('{}*{}={}'.format(i,j,i*j),end = " ")
        j += 1
    print()
    i += 1

