#用户输入
print('选择运算：')
print('1、相加\n2、相减\n3、相乘\n4、相除')

choice = int(input('输入你的选择: '))

num1 = int(input('输入第一个数字：'))
num2 = int(input('输入第二个数字: '))

if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    print(num1*num2)
elif choice == 4:
    print(num1/num2)