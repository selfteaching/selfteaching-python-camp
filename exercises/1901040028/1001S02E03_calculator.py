def jia(a,b):
    return a+b
def jian(a,b):
    return a-b
def cheng(a,b):
    return a*b
def chu(a,b):
    if b==0:
        print("分母不能为0")
    else:
        return a/b

yunsuan=input("请输入运算符1：加，2：减，3：乘，4：除。")
a=int(input("请输入数字 A:"))
b=int(input("请输入数字 B:"))

if yunsuan=="1":
    print("A+B=" , jia(a,b))
if yunsuan=="2":
    print("A-B=",jian(a,b))
if yunsuan=="3":
    print("A*B=",cheng(a,b))
if yunsuan=="4":
    print("A/B=", chu(a,b))

#print ("A+B=%s"%(a+b))
#print("A-B=%d"%(a-b))
#print("A*B=%4f"%(a*b))
#testS