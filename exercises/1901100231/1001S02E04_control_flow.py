print('''查看for ... in ... 函数打印九九乘法表请输入1
查看while函数打印九九乘法表（已去掉偶数行）请输入2
请在英文输入模式下输入
''')#对使用者提供的解释
y = "1"
while y =="1":#使程序重复运行
 x = input("请输入:")#获取要进行的操作
 if x=="1":#for...in...函数打印九九乘法表
   for i in range(1,10):#第一个数
     for j in range(1,i+1):#第二个数
        print(i,"*",j,"=",int(i)*int(j),end="\t")#打印乘法表，并利用制表符使每一列对齐
     print()#每遍历完一行执行一次换行操作     
 elif x=="2":#while函数打印九九乘法表并去掉偶数行
    a=int(1)
    b=int(1)#定义要用的两个变量
    while a<int(10):#确定a的范围
        if a%2==1:#去除偶数行
         print(a,"*",b,"=",int(a)*int(b),end="\t")
         b=b+1
         if b>a:#检验是否已打完一行乘法表，若是，则换行，a的值加一，将b的值复原
            print()
            a=a+1
            b=int(1)
        else:#若是偶数行，则令a的值再次加一，从while部分重新开始运行程序
            a=a+1   
 



                 