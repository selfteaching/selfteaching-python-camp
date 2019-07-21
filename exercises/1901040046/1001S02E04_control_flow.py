#创建一个打印九九乘法表的代码
for a in range(1,10):
    for b in range(1,a+1):
        if b<a:
           print(a,"*",b,"=",a*b,end=" ")
        else:
           print(a,"*",b,"=",a*b)
#成功！每个代码符号都是自己打出来的。虽然只有短短的六行，但是挺有成就感的。不过可能有点笨，回头去看看别人怎么写的。

#创建一个打印九九乘法表的代码,去掉偶数行。看上去依然有点笨。
for a in range(1,10):
    for b in range(1,a+1):
        while a%2!=0:
            if b<a:
               print(a,"*",b,"=",a*b,end=" ")
            else:
               print(a,"*",b,"=",a*b) 
            break