#day4 2019年7月10日 23点36分
#author:Taskow 
#Vsrsion:1.0


print ("九九乘法表")

for i in range (1,10):
    print ('第{}列'.format(i),end = '\t')
    for j in range (1,i+1):
        print ('{}*{}={}'.format (i,j,i*j ), end= '\t')
        #vserion1.0 出现的问题：
        # print ('{}*{}={}'.format (i,j,i*j ), '\t')
        #上面程序运行后不会自动回车，不是紧跟tab效果。
        '''解决办法：
           end = '\t'
        '''
    print()

#仅打印奇数行的话，
# for i in range (1,10,2):
#就ok

#问：仅打印偶数列如何解决？
'''方法1：
        for i in range (2,10,2)
        完美解决！
    方法2：
        利用教学视频中的方法，代码如下：
'''
print('跳过奇数列的九九乘法表--方法2')
for i in range (1,10):
    if i % 2 == 0:
        print ("第 %d 行"%i,end = '\t')
        for j in range (1,i+1):
            print('{}*{}={}'.format (i,j,i*j),end = '\t')
    else:
        print()

#或者方法3：

print('跳过奇数列的九九乘法表--方法3')
i = 1
while i <10:
    if i % 2 == 0:
        print ("第 %d 行"%i,end = '\t')
        for j in range (1,i+1):
            print('{}*{}={}'.format (i,j,i*j),end = '\t')
    else:
        print() 
    i +=1