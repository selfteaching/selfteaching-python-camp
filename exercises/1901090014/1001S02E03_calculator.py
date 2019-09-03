def jisuan(fuhao) :
    a=input("第一个数字")
    b=input("第二个数字")
    if fuhao == '-':
        c=int(a)-int(b)
    if fuhao == '+' :
        c=int(a)+int(b)
    if fuhao == '*' :
        c=int(a)*int(b)
    if fuhao == '/' :
       c=int(a)/int(b)
    print ("结果",c)

    return c
jisuan("+")


