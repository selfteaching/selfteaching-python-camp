print()
for i in range(0,10):
    for j in range(1,i+1): #不太明白：经过试验证明，j的range必须从1开始，为什么？
         print(i,'*',j,'=',i*j,end='   ')#print默认换行
         if i == j: #哈哈！终于想到怎么换行了！开心！
            print() 

#我先用for试一下 if的逻辑没错哈
# print()
#for i in range(0,10):
#    for j in range(1,i+1): 
#         if i % 2 == 1:   #筛选奇数
#            print(i,'*',j,'=',i*j,end='   ')#print默认换行
#            if i == j: #哈哈！终于想到怎么换行了！开心！
#            print() 


print()
x = 1
while x < 10:
    if x % 2 == 1:
        y = 1
        while y <= x:
           print(x,'*',y,'=',x*y,end='   ')
           if x == y: #条件换行
                print() 
           y += 1
    x += 1
print()