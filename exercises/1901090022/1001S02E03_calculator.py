# coding: utf-8

class Calculator:
    def desc(self):
        print("请选择运算符")
        print("1. 加")
        print("2. 减")
        print("3. 乘")
        print("4. 除")

    @staticmethod
    def addition(x, y):
        return x + y

    @staticmethod
    def subtraction(x, y):
        return x - y

    @staticmethod
    def multiplication(x, y):
        return x * y

    @staticmethod
    def division(x, y):
        return x / y
    
if __name__ == '__main__':
    operation = 1
    while operation != 0:
        print("=====================")
        input_value = input("请选择运算符对应的序号:\n1. 加\n2. 减\n3. 乘\n4. 除\n")

        x = int(input("请输入第1个数字:\n"))
        y = int(input("请输入第2个数字:\n"))

        if input_value == 1:
            print("运算 {} + {} 的结果".format(x, y))
            res = Calculator.addition(x, y)
        if input_value == 2:
            print("运算 {} - {} 的结果".format(x, y))
            res = Calculator.subtraction(x, y)
        if input_value == 3:
            print("运算 {} * {} 的结果".format(x, y))
            res = Calculator.multiplication(x, y)
        if input_value == 4:
            print("运算 {} / {} 的结果".format(x, y))
            if y == 0:
                print("错误 => 除数不能为 0 ")
                continue
            res = Calculator.division(x, y)

        print("=> {}\n<<<<<<<<<<<<<<<<<<<<<".format(res))