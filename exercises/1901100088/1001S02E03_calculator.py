x = int(input("请输入您想计算的第一个数"))
y = input("请输入计算符")
z = int(input("请输入您想计算的第二个数"))

def add(x,z):
    #print(x+z)
    print("The first number is {}, the second one is {}, and the result is {}".format(x,z,x+z))

if y == "+":
    #print(x + z)
    add(x,z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
else:
    print(x / z)