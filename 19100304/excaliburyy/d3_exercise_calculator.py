print('第一个数字')
a=input()
x=int(a)
print('第二个数字')
b=input()
y=int(b)
print('若做加法，输入q，若做减法，输入w，若做乘法，输入e，若做除于，输入r')
choice = input()
if choice == 'q':
    print(x+y)
elif choice == 'w':
    print(x-y)
elif choice == 'e':
    print(x*y)
elif choice == 'r':
    print(x/y)