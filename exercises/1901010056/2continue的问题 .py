for i in range(1,10): 
    if i % 2 ==0: 
        continue    #子句体中的 continue 语句在执行时将跳过子句体中的剩余部分并返回检验表达式
    for j in range(1,i+1):
        print(j,  '*', i, '=', i * j, sep='', end='\t')
    if j==i:
        print(end="\n") 
print(end="\n")


#while 语句用于在表达式保持为真的情况下重复地执行
i=1
while i < 10:       #"while" expression ":" suite以下
       j = 1
       while j < i + 1:
              print(j,  '*', i, '=', i * j, sep='', end='\t')
              j += 1
       print()
       i += 1



#contiue的一个简单的程序
for num in range(2, 10):
    if num % 2 == 0:                        #"if" expression ":" suite
        print("Found an even number", num)  #continue 在语法上只会出现于 for 或 while 循环所嵌套的代码
        continue                            # 它会继续执行最近的外层循环的下一个轮次。
    print("Found a number", num)            # 这一句是相当于else否则应该执行的情况  
    
#contiue的一个简单的程序中contiue的位置不同所引起程序的不同
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
    continue
    print("Found a number", num)