# Multiplication-table by WangRui
# Date:19/03/21

print("Welcome!") #打印：欢迎界面
print('-                   for                    -') #使用for...in循环

for i in range(1, 10): #给i赋值，i是1、2、3、4、5、6、7、8、9。（取值时顾头不顾尾）
    for j in range(1, i+1): #给j赋值，i是1时，j就是range(1,2),j取值就是1；i是2时，j就是range(1,3),j取值就是1、2……以此类推
        print("%d * %d = %d" % (i, j, i*j), end='\t') #打印：按照设定打印九九乘法表
    print("")


print('-                   while                    -') #使用while循环

i = 0 #行控制
j = 1 #列控制
while (i < 9): #外循环控制行数打印
	    i += 1
	    if i%2 == 0: #判断行数是偶数的时候不打印
	         continue
	    print()
	    j = 1
	    while (j <= i): #内循环控制打印列数
	        result = int(i)*int(j)
	        print(i,'*',j,'=',result,end='\t')
	        j += 1