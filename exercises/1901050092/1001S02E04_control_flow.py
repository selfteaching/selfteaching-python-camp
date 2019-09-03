
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'X',j,'=',i*j,end='\t')
    print()


i=1
while i<10:
    if i%2==0:
         print()
    else:
        for j in range(1,i+1):
                print(i,'X',j,'=',i*j,end='\t')
    i+=1        


# print(‘方法2：’) 请问为什么这里打印不出来？

for i in range (1,10):
    for j in range (1,10):
        print(i,"X",j,"=",i*j,end="\t")
        if i==j:
            print("")
            break

# 用break方法打印奇数行为什么会空出一行来
i=1
while i<10:
    if i%2==0:
         print()
    else:        
         for j in range (1,i+1):
              print(i,"X",j,"=",i*j,end="\t")
              if i==j:
                  print()
                  break
    i+=1