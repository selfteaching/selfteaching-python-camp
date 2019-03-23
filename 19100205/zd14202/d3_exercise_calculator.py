简单计算器
a=0
b=0
x="+"
a = int(input('第一个数字'))
b = int(input('第二个数字'))
x = input('选择运算符+-*/')
while x!="="
  if x=="+":
    print(a+b)
  elif x=="-":
    print(a-b)
  elif x=="*":
    print(a*b)
  elif x=="/":
    print(a/b)
  b = int(input('第二个数字'))
  x = input('选择运算符+-*/')