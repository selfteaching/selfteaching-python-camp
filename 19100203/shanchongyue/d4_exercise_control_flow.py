#参考同学的作业完成
print('''
第四天 九九乘法表
''')
print("使用for...in循环打印乘法表")
for i in range(1,10):
    print()
    for j in range(1,i+1):
        print("{}✖{}={:<4}".format(j,i,i*j),end=" ")




def odd_multiple_99(n):  #定义一个奇数的乘法表函数
        i = 1 
        while i < n:     
                if i % 2 == 0:
                        i +=1
                j=1
                while j < i+1:
                      
                        print(f'{i}*{j}=',i*j,end="  ")
                        j +=1
                i +=1
                print()    

print("使用while循环打印九九乘法表并用条件判断把偶数行除掉，输出：")
odd_multiple_99(9) 