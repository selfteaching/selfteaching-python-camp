a = input("运算符(+,-,*,/,):")
b = input("第一个数:")
c  = input("第二个数：")

b = int(b)
c = int(c)

print("a:",a, type(a))
print("b:", b, type(b), type(b))
print("c:", c, type(c), type(c))


if  a == "+":
    print(b, "+", c, "=", b + c)
elif a == "-":
    print(b, "-", c, "=", b - c)
elif a == "*":
    print(b, "*", c, "=", b * c)
elif a == "/":
    print(b, "/", c, "=", b / c)
else:
    print("无效运算符")
