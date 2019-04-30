print("1：加法 +")
print("2：减法 —")
print("3：乘法 *")
print("4：除法 /")
choice = int(input("Please input number(1/2/3/4): "))
num1 = int(input('请输入第一个数：'))
num2 = int(input('请输入第二个数：'))
if choice == 1:
    print('{} + {} = {}'.format(num1, num2, num1+num2))
elif choice == 2:
    print('{} - {} = {}'.format(num1, num2, num1-num2))
elif choice == 3:
    print('{} * {} = {}'.format(num1, num2, num1*num2))
elif choice == 4:
    print('{} / {} = {}'.format(num1, num2, num1/num2))
else:
    print('输入有误')