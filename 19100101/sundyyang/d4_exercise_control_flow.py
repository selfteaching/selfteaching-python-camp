#output “Multiplication Table” by “for xx in"

for a in range (1,10): #遍历1-10数字序列
    for b in range (1,a+1): #遍历1-“i+1”数字序列
        print(a,"*",b,"=",a*b,end = "\t") #打印

print("\n") #空行
print("\n") #空行

a = 1 #赋值
while a <= 9: #在<=9内循环
    b = 1
    a = a + 1
    while b <= a:
        if a % 2 != 0:
            if b < a:
                print(a,"*",b,"=",a*b,end = "\t")
                b = b + 1
            else:
                print(a,"*",b,"=",a*b,end = "\t")
                b = b + 1
        else:
            b = b + 1
