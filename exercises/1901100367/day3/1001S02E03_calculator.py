print('请选择你想做的运算')
print('加法请按数字1')
print('减法请按数字2')
print('乘法请按数字3')
print('除法请按数字4')
faze=input('请输入你想做的运算法则,输入对应的数字[1,2,3,4]:')
print(faze)

print('下面开始运算')
num1=float(input('请输入第一个数字:'))
num2=float(input('请输入第二个数字:'))

if faze=='1':
    print(num1 + num2)

if faze=='2':
    print(num1 - num2)

if faze=='3':
    print(num1 * num2)

if faze=='4':
    print(num1 / num2)






