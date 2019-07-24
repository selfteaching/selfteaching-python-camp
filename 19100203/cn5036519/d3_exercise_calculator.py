# 实现一个支持加、减、乘、除功能的计算器
# 加法运算
def add(*args):
    # print(args)    #返回一个元组
    sum = 0
    for e in args:
        sum += e
    return sum
# 减法运算
def subtract(*args):
    difference = 0
    index = 0
    while index < len(args):
        if index == 0:
            difference = args[index]
        else:
            difference -= args[index]
        index += 1
    return difference
# 乘法运算
def multiply(*args):
    multiplication = 1
    for e in args:
        multiplication *= e
    return multiplication
# 除法运算
def divide(*args):
    division = 0
    index = 0
    while index < len(args):
        if index == 0:
            division = args[index]
        else:
            division /= args[index]
        index += 1
    return division

operator_options = int(input("请选择：\n01 加法\n02 减法\n03 乘法\n04 除法"))
if operator_options == 1:
    # 加法运算
    nums= input("请输入加法表达式：").replace(' ','').split("+")
    size = len(nums)
    for i in range(0,size):
        nums[i] = int(nums[i])
    if size == 2:
        print(add(nums[0],nums[1]))
    elif size == 3:
        print(add(nums[0],nums[1],nums[2]))
    elif size == 4:
        print(add(nums[0],nums[1],nums[2],nums[3]))
    else:
        print("脑容量有限，计算不过来了！")

elif operator_options == 2:
    # 减法运算
    nums= input("请输入减法表达式：").replace(' ','').split("-")
    size = len(nums)
    for i in range(0,size):
        nums[i] = int(nums[i])
    if size == 2:
        print(subtract(nums[0],nums[1]))
    elif size == 3:
        print(subtract(nums[0],nums[1],nums[2]))
    elif size == 4:
        print(subtract(nums[0],nums[1],nums[2],nums[3]))
    else:
        print("脑容量有限，计算不过来了！")
elif operator_options == 3:
    # 乘法运算
    nums= input("请输入乘法表达式：").replace(' ','').split("*")
    size = len(nums)
    for i in range(0,size):
        nums[i] = int(nums[i])
    if size == 2:
        print(multiply(nums[0],nums[1]))
    elif size == 3:
        print(multiply(nums[0],nums[1],nums[2]))
    elif size == 4:
        print(multiply(nums[0],nums[1],nums[2],nums[3]))
    else:
        print("脑容量有限，计算不过来了！")   
elif operator_options == 4:
    # 除法运算
    nums= input("请输入除法表达式：").replace(' ','').split("/")
    size = len(nums)
    for i in range(0,size):
        nums[i] = int(nums[i])
    if size == 2:
        print(divide(nums[0],nums[1]))
    elif size == 3:
        print(divide(nums[0],nums[1],nums[2]))
    elif size == 4:
        print(divide(nums[0],nums[1],nums[2],nums[3]))
    else:
        print("脑容量有限，计算不过来了！")
else:
    print("出错了")