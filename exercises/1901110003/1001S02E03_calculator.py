def add(string):
    
    total = 0

    numbers = []

    numbers += string.split("+")

    for num in numbers:

        total += int(num)

    print("{0}={1}".format(string,total))



def minus(string):

    result = 0

    numbers = []

    numbers += string.split("-")

    result = int(numbers[0])

    numbers.pop(0)

    for num in numbers:

        result -= int(num)

    print("{0}={1}".format(string,result))



def times(string):

    total = 1

    numbers = []

    numbers += string.split("*")

    for num in numbers:

        total *= int(num.strip())

    print("{0}={1}".format(string,total))



def division(string):

    result = 0

    numbers = []

    numbers += string.split("/")

    result = int(numbers[0])

    numbers.pop(0)

    for num in numbers:

        result /= int(num.strip())

    print("{0}={1}".format(string,result))



if __name__ =="__main__":

    print("1：add")

    print("2：minus")

    print("3：times")

    print("4：division")

    method = input("Please input number(1/2/3/4): ")

    if method == "1":

        string = input("input：")

        add(string)

    elif method == "2":

        string = input("input：")

        minus(string)

    elif method == "3":

        string = input("input：")

        times(string)

    elif method == "4":

        string = input("input：")

        division(string)

    else:

        print("The string you input is error.")