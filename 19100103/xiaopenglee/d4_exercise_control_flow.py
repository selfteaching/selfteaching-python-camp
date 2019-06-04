# Filename : d4_exercise_control_flow.py
# author by : lxp
 
# 打印乘法口诀表

#九九乘法表for循环
print("九九乘法表")
for i in range(1,10):
    for a in range(1,i+1):
        print(i,"x",a,"=",i*a," ",end="")
    print("")

#九九乘法奇数表while循环
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


