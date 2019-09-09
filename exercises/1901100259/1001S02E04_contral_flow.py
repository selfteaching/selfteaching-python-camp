#1.使用 for...in 循环打印九九乘法表.
for a in [1,2,3,4,5,6,7,8,9]:
    for b in range (1,a+1):
        print(a,"*",b,"=",a*b,"\t" ,end="")
    print("")
    
    

#2.使用 while 循环打印九九乘法表并用条件判断把偶数行去除掉.
a=1
while a<=9:
    for b in range(1,a+1):  
        print(a,"*",b,"=",a*b,"\t" ,end="", )
    a=a+2
    print("")
else:
    print("very gond!")



#3.使用 while 循环打印九九乘法表并用条件判断把奇数行去除掉.
a=0
while a<9:
    for b in range(1,a+1): 
        print(a,"*",b,"=",a*b,"\t" ,end="", )
    a=a+2
    print("")
else:
    print("very gond!")
