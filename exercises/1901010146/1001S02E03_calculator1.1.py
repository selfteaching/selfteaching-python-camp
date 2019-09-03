def add(addf):
    addf = a+b
def sub(subs):
    subs = a-b
def mul(muls):
    muls = a*b
def div(divs):
    divs = a/b
print("这是一个计算器")
a = int(input("请输入第一个数字："))
x = str(input("选择哪种运算 1:+ 2:- 3:* 4:/"))
b = int(input("请输入第二个数字："))
if x == "+":
    print(add(addf=))
elif x == "-":
    print(sub(subs))
elif x == "*":
    print(mul(muls))
else:
    print(div(divs))
