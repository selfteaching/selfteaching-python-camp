for hang in range(1,10):#表示从1开始一共有9行
    for lie in range(1,hang+1):#表示列，每行的列数等于行数
            ji=hang*lie#九九乘法表就是两个数相乘得出一个积
            print("{0}*{1}={2}{3}".format(hang,lie,ji,"\t"),end="")#"\t"是转义字符，意为向右移动一位使表格排列整齐
    print("")
print("只打印奇数行")
for hang in range(1,10):
  while hang%2==1:
    for lie in range (1,hang):
        print(hang,"*",lie,"=",hang*lie,end='\t')
    print(hang,"*",hang,"=",hang*hang)
    break