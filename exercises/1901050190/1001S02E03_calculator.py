a = input("�����(+,-,*,/,):")
b = input("��һ����:")
c  = input("�ڶ�������")

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
    print("��Ч�����")
