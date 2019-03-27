#这是一个返回值的表示测试，如果x大于2则返回x，如果x小于等于2，则返回0.（成功）

def test(x):#这里用来定义返回规则
    if x > 2:
        return x
    else:
        return 0

x = int(input("shuruyigeshuzi:"))#这里进行输入，限制输入值为整数
y = test(x)#定义y等于返回的值
print(y)#输出返回的值