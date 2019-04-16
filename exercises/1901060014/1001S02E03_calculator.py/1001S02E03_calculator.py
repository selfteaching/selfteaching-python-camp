def add(string):
    tmp = 0
    numbers =[]
    numbers += string.split("+")
    for i in numbers:
        tmp += int(i.strip())
    print("{0} = {1}".format(string, tmp))


def subtraction(string):
    numbers= []
    numbers += string.split("-")
    tmp = int(numbers[0].strip())
    numbers.pop(0)
    for i in numbers:
        tmp -= int(i.strip())
    print("{0} = {1}".format(string,tmp))

def multiplication(string):
    numbers= []
    numbers += string.split("*")
    tmp = int(numbers[0].strip())
    numbers.pop(0)
    for i in numbers:
        tmp *= int(i.strip())
    print("{0} = {1}".format(string,tmp))


def division(string):
    numbers= []
    numbers += string.split("/")
    tmp = int(numbers[0].strip())
    numbers.pop(0)
    for i in numbers:
        tmp /= int(i.strip())
    print("{0} = {1}".format(string,tmp))


if __name__ == '__main__':
    print("*************************")
    print("      Paradox5656    ")
    print("*************************")
    chose = input("选择你要的计算方式，1/加法 ，2/减法 ， 3/乘法， 4/除法：")
    if chose == "1":
        tmp = input("请输入你要计算的数字")
        add(tmp)
    elif chose == '2':
        tmp = input("请输入你要计算的数字")
        subtraction(tmp)
    elif chose == '3':
        tmp = input("请输入你要计算的数字")
        multiplication(tmp)
    elif chose == '4':
        tmp = input("请输入你要计算的数字")
        division(tmp)
    else:
        print("你输入有误，请重新")