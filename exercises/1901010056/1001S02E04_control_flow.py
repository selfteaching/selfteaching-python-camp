#for循环    "for"  target_list目标列表  "in"  expression_list表达式列表  ":" suite
#          ["else" ":" suite]     当所有项被耗尽时,else 子句的子句体如果存在将会被执行，并终止循环。
#系统将为 expression_list 的结果创建一个迭代器，然后将为迭代器所提供的每一项执行一次子句体，具体次序与迭代器的返回顺序一致。

for i in range(1, 10):                #对于表达式列表，中的1到9这九个数字，都会执行下面的子句体一次  
    for j in range(1, i+1):           #第二个for循环相当于第一个for循环的suite
        print('{}x{}={}\t'.format(j, i, i*j), end='') 
    print(6)                          #相当于else语句。起到了在所有项都耗尽的情况下，终止循环的作用


#上面的式子也可以写成
for i in range(1, 10): 
    for j in range(1, i+1):print('{}x{}={}\t'.format(j, i, i*j), end='') 
    print()
    

#由于print()函数默认结尾会自动增加换行符，在打印乘法表时，需要将print（）函数的结尾符配置为制表符

for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+"*"+str(i)+"="+str(i*j),end=" ")
    print(end="\n")                                     #自己简化的第一个程序，基于，理解了for循环的定义



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
        print() 
print()



