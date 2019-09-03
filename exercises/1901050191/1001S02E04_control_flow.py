for n in range(1 , 10):  #n这个变量属于1-10的等差数列内的数字
    for i in range(1 , 10):  # i这个变量属于等差数列内的数字。
        if n >= i:     #如果n的值大于等于i的值
            print(n, '*', i, '=',  n  *  i, end='\t')     #输出n*i=的数值
            continue       #返回条件，继续当前的循环
        else:     #如果是其他情况
            break #进入下一个语句判断
    print()
n = 1 #把1赋予变量n
while n < 10 : #且n是10以内的数字
    if n %2 ==0: #第一种情况，当n是偶数的时候    
        print() #直接换行
    else:   #其他情况下，即当n是奇数1.3.5.7.9的情况下
        for i in range(1 , n + 1): #取变量i,i在1--n范围内变化，即当n=5的时候，i在1-5之间变换
            print(n, '*', i, '=',  n  *  i, end='\t') #输出并换行
    n = n + 1 #处理条件，计数器+1
    continue  #continue 好像有没有都一样    