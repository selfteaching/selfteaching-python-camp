print("九九乘法表：")

for i in range (1,10):
    for j in range(i):
        j=j+1
        print("%d*%d=%-3d" % (i,j,i*j),end="")
    print("")

print("----------------------- 华丽丽的分割线 ------------------------")

print("去除偶数行的九九乘法表:")
i = 1
while i < 10:
       j = 1
       while j < i + 1:
       	      if i%2 == 0:
                    break
              print(i,  '*', j, '=', i * j, sep='', end='\t')
              j += 1

       print()
       i += 1