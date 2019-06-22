for x in range(1,10): #X为行数1-9
    for y in range(1,x+1): #Y为列数小于等于行数
        print(str(x)+'*'+str(y)+'='+str(x*y),end='\t') #end='\t')删除自动换行动作加定位点
    print() #换行
x = 1       #x为行数
while x <= 9:   #循环9次
    y = 1       #列数
    while y <= x: #列数小于等于行数
        if x % 2 == 0: #如果行数为偶数
            break
        print(str(x)+'*'+str(y)+'='+str(x*y),end='\t') 
        y=y+1 #简化可写成y+=1
    x=x+1
    print()
        