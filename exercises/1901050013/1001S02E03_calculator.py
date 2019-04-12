def COUNT(count_one,count_two,operation):
    if operation == '+':
        print(count_one, "+" ,count_two, "=" ,(count_one + count_two))
    elif operation =="-":
        print(count_one,"-",count_two,"=",(count_one - count_two))
    elif operation =="*" or operation =='x':
        print(count_one,'*',count_two,"=",(count_one * count_two))
    elif operation == '/' :
        print(count_one,'/',count_two,"=",(count_one / count_two))
    elif operation == '%':
        print(count_one,'%',count_two,'=',(count_one % count_two))
    else:
        print("error")


while_condition = True
while while_condition:
    count_one = int(input("请输入第一个数：")) 
    count_two = int(input("请输入第二个数："))
    operation = input("请输入要执行的四则运算(+-*/):")
    if COUNT(count_one,count_two,operation) == 1:
        print("error operation")
    else:
        while True:
            Continue = input("是否继续? y/n: ")
            if Continue == 'y':
                print("user continue")
                break
            elif Continue == "n":
                print("user termination")
                while_condition = False
                break
            else:
                print("user input the error option")