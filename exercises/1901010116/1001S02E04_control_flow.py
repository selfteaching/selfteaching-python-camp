#使用for ... in 循环打印九九乘法表
def multiply(x,y):
    return x*y

str1 = "作业一：for ... in 循环打印九九乘法表"
str2 = "作业二：while 循环打印九九乘法表奇数行"

print(str1.center(120,'-'))

for n in range(1,10):
    for i in range(1,n+1):
            if i < n:
                print(n,'*',i,"=",multiply(i,n),end='\t')
            else:
                print(n,'*',i,"=",multiply(i,n))

#使用while循环打印九九乘法表
#用条件判断把偶数行去除掉
print(str2.center(120,'-'))

a = 1
while a < 10:
    b = 1
    while b <= a and a % 2 != 0:
        print(a,'*',b,"=",multiply(a,b),end='\t')
        b += 1
    else:
        print()     
        a += 1
