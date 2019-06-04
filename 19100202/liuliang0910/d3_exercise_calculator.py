# 用来做注释的，单行哦，就是解释这个代码是什么意思

""" 多行字符串用三个引号
    包裹，也常被用来做多
    行注释
""" 


# 看了半天，似懂非懂，但是我真的想不到怎么做一个计算器咯，所以我就抄了google的，然后附上注释吧

def add(string):                                #定义加法
    tmp = 0
    numbers = []
    numbers += string.split("+")               #对用户输入的数字以+号做分割，写入到列表里。
    for i in numbers:                          #遍历列表。
        tmp += int(i.strip())                  #先对遍历的对象i,去除空格后，得出结果tmp = i + tmp
    print("{0} = {1}".format(string, tmp))     #打印结果tmp


def subtraction(string):                        #定义减法
    numbers = []
    numbers += string.split("-")                #对用户输入的数字以-号做分割，写入到列表里。
    tmp = int(numbers[0].strip())               #取列表的第一个数字给tmp
    numbers.pop(0)                              #因为第一个值给了tmp 所以删除第一个值。
    for i in numbers:                           #遍历numbers
        tmp -= int(i.strip())                   #得出结果tmp ，每次循环都删除第一个值然后相减。
    print("{0} = {1}".format(string, tmp))


def multiplication(string):                     #定义乘法
    numbers = []
    numbers += string.split("*")                #对用户输入的数字以*号做分割，写入到列表里。
    tmp = int(numbers[0].strip())               #取列表的第一个数字给tmp
    numbers.pop(0)                              #因为第一个值给了tmp 所以删除第一个值。
    for i in numbers:                           #遍历numbers
        tmp *= int(i.strip())                   #得出结果tmp ，每次循环都删除第一个值然后相乘。
    print("{0} = {1}".format(string, tmp))


def division(string):                            #定义除法
    numbers = []
    numbers += string.split("/")                 #对用户输入的数字以/号做分割，写入到列表里。
    tmp = int(numbers[0].strip())                #取列表的第一个数字给tmp
    numbers.pop(0)                               #因为第一个值给了tmp 所以删除第一个值。
    for i in numbers:                            #遍历numbers
        tmp /= int(i.strip())                    #得出结果tmp ，每次循环都删除第一个值然后相除。
    print("{0} = {1}".format(string, tmp))


if __name__ == '__main__':                       #定义执行方式，当执行脚本本身，执行如下代码。
    print("******************************")
    print("          计算器")
    print("******************************")
    chose = input("选择你要的计算方式，1/加法 ，2/减法，3/乘法，4/除法: ")
    if chose == "1":
        tmp = input("请输入你要计算的数字:")
        add(tmp)
    elif chose == '2':
        tmp = input("请输入你要计算的数字:")
        subtraction(tmp)
    elif chose == '3':
        tmp = input("请输入你要计算的数字:")
        multiplication(tmp)
    elif chose == '4':
        tmp = input("请输入你要计算的数字:")
        division(tmp)
    else:
        print("你输入的有误，请重新输入")


