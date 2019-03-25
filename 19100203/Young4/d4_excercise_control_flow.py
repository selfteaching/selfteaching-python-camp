#utf=8
#九九乘法表

print('''
Young4's 九九乘法表
''')

print("使用for...in循环打印九九乘法表，输出：")
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}=',i*j,end='\t')
    print()

def odd_multiple_99(n):  #定义一个奇数的乘法表函数
        i = 1 
        while i < n:     
                if i % 2 == 0:
                        i +=1
                j=1
                while j < i+1:
                        print(f'{i}*{j}=',i*j,end='\t')
                        j +=1
                i +=1
                print()    

#Call the odd_multiple_99(n)
print("使用while循环打印九九乘法表并用条件判断把偶数行除掉，输出：")
odd_multiple_99(9)