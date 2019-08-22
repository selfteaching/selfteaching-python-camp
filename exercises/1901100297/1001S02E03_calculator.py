print('我们来做四则运算，请选择你的运算类型')
print('1，加法')
print('2，减法')
print('3，乘法')
print('4，除法')

choice = input("选择运算类型（1/2/3/4）")

if choice =='1':
   print("第一个数")
   a=input()
   x=int(a)
   print('第二个数')
   b=input()
   y=int(b)
   print("结果",x+y)

elif choice =='2':
   print("第一个数")
   a=input()
   x=int(a)
   print('第二个数')
   b=input()
   y=int(b)
   print("结果",x-y)

elif choice =='3':
   print("第一个数")
   a=input()
   x=int(a)
   print('第二个数')
   b=input()
   y=int(b)
   print("结果",x*y)

elif choice =='4':
   print("第一个数")
   a=input()
   x=int(a)
   print('第二个数')
   b=input()
   y=int(b)
   print("结果",x/y)
