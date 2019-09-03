print('九九乘法表')

for a in range(1,10):
    b = 0
    while b < a:
        b = b + 1
        print (a,'*',b,'=',a*b,end='    ')
    else:
        print ('\n')

print('奇数行，九九乘法表')
for x in range(1,10):
    y = 0
    
    while y < x:
        y = y + 1     
        if x%2 == 0:
            break
        else:
            print (x,'*',y,'=',x*y,end='    ')        
        
    else:
        print ('\n')

# 学习要点 for是在一个列表中循环输出
#         while是在某个条件下循环输出
#         range 是选定某个范围内
#         end'  '是以空格中断换行，end'\n'是换下一行
#         break 在此条件下中断循环