#使⽤用for...in循环打印九九乘法表

#for循环    "for"  target_list目标列表  "in"  expression_list表达式列表  ":" suite
#          ["else" ":" suite]     当所有项被耗尽时,else 子句的子句体如果存在将会被执行，并终止循环。
#系统将为 expression_list 的结果创建一个迭代器，然后将为迭代器所提供的每一项执行一次子句体，具体次序与迭代器的返回顺序一致。

for i in range(1, 10):                #对于表达式列表，中的1到9这九个数字，都会执行下面的子句体一次  
    for j in range(1, i+1):           #第二个for循环相当于第一个for循环的suite
        print('{}x{}={}\t'.format(i, j, i*j), end='') 
    print()                           #相当于else语句。起到了在所有项都耗尽的情况下，终止循环的作用

    

#print()函数默认结尾会自动增加换行符，换行符和制表符的写法只有在引号内才起作用，才会被视为一个字符。
#注意：换行符和制表符的写法只有在引号内才起作用，才会被视为一个字符。 
#一些拓展\n换行符，纵向制表符\v
#end=" "会使函数关闭在输出中自动包含换行的默认行为
#sep='' 改变各字符串间隔
#.format()是占位函数，{}x{}={}表示先在{}这里占位

#便于理解
#for i in range(1,10):
#     for j in range(1,i+1):
#        print(str(j)+"*"+str(i)+"="+str(i*j),end=" ")
#    print(end="\n")                                     



i=1
while i < 10:
       j = 1
       while j < i + 1:
       	      if i%2 == 0:
               break  #参考这个https://www.runoob.com/python/python-break-statement.html
              print(i, '*', j, '=', j * i, sep='', end='\t')
              j += 1   #自增写法，equals j = j + 1 这个可以看一下https://www.runoob.com/python/python-while-loop.html
       print()
       i += 1

    
#for i in range(1,10): 
#    if i % 2 ==0: 
#        continue    
#    for j in range(1,i+1):
#        print(str(j)+"*"+str(i)+"="+str(j*i),end=" ")
#    if j==i:
#        print() 
#print()



