# 定义函数
# 函数内部的程序码，若是没有做函数呼叫，就不会执行
# def multiply(n1,n2):
#     print(n1*n2)  #可以去掉
#     return n1*n2
# # 呼叫函数
# value=multiplyy(3,4)+multiply(10,5) #(3*4)+(10*5)
# print(value)

# 程序的包装  函数可以用来做程序的包装：同样的逻辑可以重复利用
def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)

calculate(10)
calculate(20)