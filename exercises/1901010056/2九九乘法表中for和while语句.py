for i in range(1,10): 
    if i % 2 ==0:  continue                                                 #  "if"  expression  ":"  suite                                          
    for j in range(1,i+1):print(j,  '*', i, '=', i * j, sep='', end='\t')   #这个for循环相当于第一个if语句隐藏的 "else"   ":"  suite    
    if j==i:print(end="\n")                                                 #这个if语句项也相当于第一个for语句的suite
print(end="\n")



#while语句    "while" expression ":" suite     ["else" ":" suite]
#while 语句用于在表达式保持为真的情况下重复地执行
#这是一个嵌套条件循环
i=1
while i < 10:                      #"while" expression ":" suite以下
       j = 1                       #从这一行开始，都是while的suite
       while j < i + 1 :            
              print(j,  '*', i, '=', i * j, sep='', end='\t')
              j += 1
       print()
       i += 1


n = 1000               #以条件为基础的循环
a, b = 0, 1             #
while a < n:               #如果其值为真就执行第一个子句体，这将重复地检测表达式
    print(a, end=' ')
    a, b = b, a+b          #如果表达式为假，有else存在的话，将会被被执行，并且终止循环。如果else不存在的话，直接终止循环
    print()                 #print()放在子句体里面,出来的数字时竖列.放在外面，或者，不写出来的数字时横列。 


