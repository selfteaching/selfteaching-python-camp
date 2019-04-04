for i in range(1, 10): 
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='') 
    print()

#由于print()函数默认结尾会自动增加换行符，在打印乘法表时，需要将print（）函数的结尾符配置为制表符

for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+"*"+str(i)+"="+str(i*j),end=" ")
    if j==i:
        print(end="\n")
print(end="\n")



i=1
while i < 10:
       j = 1
       while j < i + 1:
       	      if i%2 == 0:
               break
              print(j,  '*', i, '=', i * j, sep='', end='\t')
              j += 1
       print()
       i += 1

    
for i in range(1,10): 
    if i % 2 ==0: 
        continue    
    for j in range(1,i+1):
        print(str(j)+"*"+str(i)+"="+str(j*i),end=" ")
    if j==i:
        print(end="\n") 
print(end="\n")



