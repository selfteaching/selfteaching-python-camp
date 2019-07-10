# 土法计算器--甲
print ("请系好安全带，我是你土法计算器甲大爷")
print ("请人类依次输入数据:")

# 用户输入
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

# 结果输出
print ((num1+num2),(num1-num2),(num1*num2),(num1/num2))
print ("上面四个数字依次为加减乘除的运算结果")


# 土法计算器--乙
# 用户输入选择
choice = input("输入你的选择(加/减/乘/除):")

# 用户输入数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

# 结果输出 
if choice == '加':
  print ("第一个数字","+","第二个数字","=",num1+num2)
 
elif choice == '减':
  print ("第一个数字","+","第二个数字","=",num1+num2)
 
elif choice == '乘':
  print ("第一个数字","+","第二个数字","=",num1+num2)
 
elif choice == '除':
  print ("第一个数字","+","第二个数字","=",num1+num2)
else:
   print("您输入的有误")
   print("人生不能重来，所以您没有下次输入的机会了")
   print("死机了")
   print("再见！！！")