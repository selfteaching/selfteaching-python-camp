#contiue的一个简单的程序
for num in range(2, 10):
    if num % 2 == 0:                       #"if" expression ":" suite
        print("Found an even number", num) #continue 在语法上只会出现于 for 或 while 循环所嵌套的代码
        continue                           # 它会继续执行最近的外层循环的下一个轮次。    
    print("Found a number", num)           # 这一句是相当于else否则应该执行的情况         

#contiue的一个简单的程序中contiue的位置不同所引起程序的不同
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
    continue
    print("Found a number", num)

    end="\n"