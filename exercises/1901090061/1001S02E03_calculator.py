x=input('请输入第一个数字：')
y=input('请输入第二个数字：')
num_1=int(x)
num_2=int(y)
result_1=num_1+num_2
result_2=num_1-num_2
result_3=num_1*num_2
result_4=num_1/num_2
op_1=input('请选择运算方式：1=加法，2=减法，3=乘法，4=除法：')
op=int(op_1)
if op==1:
    print(result_1)
elif op==2:
    print(result_2)
elif op==3:
    print(result_3)
elif op==4:
    print(result_4)
else:
    print("数据输入错误！")