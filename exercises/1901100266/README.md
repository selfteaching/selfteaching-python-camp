Task 1 It hinders my  courage a bit for the unknown running environment, but it won't stop me.

Task 2

**Python: Select Interpreter**, that interpreter is applied when right-clicking a file and selecting **Python: Run Python File in Terminal**. The environment is also activated automatically when you use the **Terminal: Create New Integrated Terminal** command.

Use the **Terminal: Create New Integrated Terminal** command after VS Code is running. 

`print()` tells Python to display or output whatever we put in the parentheses.

Task 4

print(str('去掉偶数行的九九乘法表'))

i = 1 #是把i的起始值设为1

while i < 10:

  if i % 2 == 0:

​    print()

  else:

​    for j in range(1,i+1):

​      print(i, '*' , j,"=",i * j,end='\t'

  i += 1 #i=i+1,相当于把上一个的i再加1，重新赋值给了新的i

