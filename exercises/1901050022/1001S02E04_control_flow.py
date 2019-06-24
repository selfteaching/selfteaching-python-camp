# Filename : 1001S02E04_control_flow.py
# author by : kidswonder

print('''
DAY4 九九乘法表
''')
print("使用for...in循环打印乘法表")
for i in range(1,10):
    for a in range(1,i+1):
        print(i,"x",a,"=",i*a," ",end="")
    print("")





    print("九九乘法奇数表")
 i=1
while i<10:
    if i%2==0:
        i=i+1
        continue
    a=1
    while a<i+1:
         print(i,"*",a,"=",i*a,"",end="")
         a=a+1
    print("",end="\n")
    i=i+1