'''
题目：使用for循环打印九九乘法表。
思路：
    1、通过看输出的九九乘法表，发现规律：
        （1）左边数*右边数=乘积
            左边数都是当前行，即第一行是1*1 ，第二行是2*1，第三行是3*1...,总共9行
            右边数都是每次都是从1开始，它的列数正好对应的行数，即第1行是1列，第2行是2列

'''
for line in range(1,10):
    for column in range(1,line+1):
        print("{line}*{column}={result}".format(line=line,column=column,result=line*column), end='   ')
    print()



# 题目：使用while循环打印九九乘法表并用条件判断把偶数行去除掉。
line = 1
while line<10:
    if line%2 == 0:
        line += 1
        continue
    else:
        column = 1
        while column<line+1:
            print("%d*%d=%d" % (line, column, line*column),end="   ")
            column += 1
        print()
        line += 1



'''
题目：实现一个支持加、减、乘、除功能的计算器
说明：在昨天的代码上优化了一点，不过，还是只能处理简单的运算，比如带有小括号的运算还是会报错。
'''
# 加法运算
def add(*args):
    # print(args)    #返回一个元组
    sum = 0
    for e in args[0]:   #这块写死了
        sum += e
    return sum
# 减法运算
def subtract(*args):
    difference = 0
    index = 0
    while index < len(args[0]):
        if index == 0:
            difference = args[0][index]
        else:
            difference -= args[0][index]
        index += 1
    return difference
# 乘法运算
def multiply(args):   
    if isinstance(args, list):
        multiplication = 1
        for e in args:
            multiplication *= e
        return multiplication
# 除法运算
def divide(args):
    if isinstance(args, list):
        division = 0
        index = 0
        while index < len(args):
            if index == 0:
                division = args[index]
            else:
                division /= args[index]
            index += 1
        return division
# 将列表中的每个元素转换成int
def element_convert_int(li):
    for i in range(len(li)):
        li[i] = int(li[i])

# 图形界面
while 1:
    operator_options = int(input("请选择(序号)：\n01 加法\n02 减法\n03 乘法\n04 除法\n05 退出\n"))
    if operator_options == 1:
        # 加法运算
        nums= input("请输入加法表达式：").replace(' ','').split("+")
        element_convert_int(nums)
        print(add(nums))
    elif operator_options == 2:
        # 减法运算
        nums= input("请输入减法表达式：").replace(' ','').split("-")
        element_convert_int(nums)
        print(subtract(nums))   
    elif operator_options == 3:
        # 乘法运算
        nums= input("请输入乘法表达式：").replace(' ','').split("*")
        element_convert_int(nums)  
        print(multiply(nums)) 
    elif operator_options == 4:
        # 除法运算
        nums= input("请输入除法表达式：").replace(' ','').split("/")
        element_convert_int(nums)  
        print(divide(nums))
    elif operator_options == 5:          
        print("欢迎下次光临！")
        break
    else:
        print("不支持其他运算！")
        break