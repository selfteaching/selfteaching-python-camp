#作业1：
###使用python默认的结尾换行符
for x in range(1,10):
    for y in range(1,1+x):
        print(str(x)+"*"+str(y)+"="+str(x*y),end=" ")
    print("")


###将python默认的结尾换行符换为制表符
for x in range(1,10):
    for y in range(1,1+x):
        print(str(x)+"*"+str(y)+"="+str(x*y),end=" ")
    print("",end="\t")


#作业2：
for x in range(1,10):
    for y in range(1,1+x):
            if x % 2 == 0:
                print("",end="\t")
            else:
                print(str(x)+"*"+str(y)+"="+str(x*y),end="\t")

