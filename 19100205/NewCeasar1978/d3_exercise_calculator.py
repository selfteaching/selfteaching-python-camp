a = int(input("""
1：加法
2：减法
3：乘法
4：除法
请输入您要进行的计算:"""))
i = int(input("请输入第一个数字："))
j = int(input("请输入第二个数字："))
if a == 1:
    print(i ,'+',j,'=',i+j)
elif a == 2:
    print(i,"-",j,'=', i-j)
elif a == 3:
    print(i,'*',j,'=',i*j)
elif a== 4:
    print(i,'/',j,'=',i/j)
else:
    print("输入错误！")







