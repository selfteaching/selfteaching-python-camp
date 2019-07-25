import re
symlist = ["/","*"]
string=input("请输入运算等式")
#re.findall(r"\d+\.?\d*",string)
num = (re.findall(r"\d+\.?\d*",string))     #获取列式中的数字
print(num)
sym = re.findall(r"\W*",string)          #获取列式中的运算符
sym.remove("")
for i in sym:
    sym.remove("")

print(sym)
#symbol = re.findall(r"\[/-]*",string)
#print (re.findall(r"\\+?",string))list(set(a).difference(set(b)))


def caculator(num,sym):
    num1 = num
    sym1 = sym                                                    #now I know the sentences is useless
    if len(num1) - len(sym1)!=1:
        return False
    while set(sym1).intersection(set(symlist))!=set():              #caculate until the symbol is none of * or /
        a = set(sym1).intersection(set(symlist))                   #use it to debug ,it is also useless
        print(a)
        for i in sym1:
            print (i)                                           #check the list is correct
            n = sym.index(i)
            if i == "*" or i == "/":                             #the multipy and the divided caculator is privilege
                if i == '*':
                    num1[n] = str(float(num1[n]) * float(num1[n+1]))   #multiply or divided
                    print (num[n])
                    del num1[n+1]
                    del sym[n]
                    print(sym1)
                    print(num1)
                elif i == '/':
                   num1[n] = str(float(num[n]) / float(num[n+1]))   #multiply or divided
                   print (num[n])
                   del num1[n+1]
                   del sym[n]
                   print(sym1)
                   print(num1)
    while sym1!=[]:                                                #caculate until the symbol is none
        for i in sym1:
            print (i)                                                #check the list is correct
            n = sym.index(i)
            if i == "+" or i == "-":                                  
                if i == '+':
                    num1[n] = str(float(num1[n]) + float(num1[n+1]))   #plus or abtract
                    print (num[n])
                    del num1[n+1]
                    del sym[n]
                    print(sym1)
                    print(num1)
                if i == '-':
                   num1[n] = str(float(num[n]) - float(num[n+1]))   #plus or abtract
                   print (num[n])
                   del num1[n+1]
                   del sym[n]
                   print(sym1)
                   print(num1)
     
    return float(num1[0])   

                
result = caculator(num,sym)
print(result)