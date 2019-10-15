#用vscode打开，并使用Python编写⼀一个支持加、减、乘、除功能的计算器，支持输⼊参数，支持输出结果。
def findAndCheckOperator(stringToCalculate: str):
    operator = ""
    if stringToCalculate.find("+") != -1:
        operator = "+"
    elif stringToCalculate.find("-") != -1:
        operator = "-"
    elif stringToCalculate.find("*") != -1:
        operator = "*"
    elif stringToCalculate.find("/") != -1:
        operator = "/"
    else:
        print(operator, " is illegal.")
    return operator

def getOperands(stringToCalculate: str, operator: str): 
    numberStrList = stringToCalculate.split(operator)
    numbers = []
    for numberStr in numberStrList:
        # 转换为整数
        numbers.append(int(numberStr))
    return numbers

def doCalculate(operator: str, operands):
    result = 0
    if operator == "+":
        # do add.
        for number in operands:
            result += number
    elif operator == "-":
        # do minus.
        result = operands[0]
        subOperands = operands[1:len(operands)]
        for number in subOperands:
            result -= number
    elif operator == "*":
        # do times.
        result = 1
        for number in operands:
            result *= number
    elif operator == "/":
        # do div.
        result = operands[0]
        subOperands = operands[1:len(operands)]
        for number in subOperands:
            result /= number
    else:
        print(operator, " is illegal")
    return result

# 主入口
if __name__ == "__main__":
    print("Usage: Input a string to calculate.")
    print("       e.g. 1+2+3")
    inputStr = input("Input: ")
    # print("Input is ", str)
    # check str
    operator = findAndCheckOperator(inputStr)
    print("Operator is ", operator)
    # get all operands
    operands = getOperands(inputStr, operator)
    print("operands: ", operands)
    # calculate
    result = doCalculate(operator, operands)
    # print result
    print(inputStr, "=", result)