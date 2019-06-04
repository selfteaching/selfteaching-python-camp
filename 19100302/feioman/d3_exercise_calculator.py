import re
def md(l,x):
    a = l.index(x)
    if x == '*' and l[a + 1] != '-':
        k = float(l[a - 1]) * float(l[a + 1])
    elif x == '/' and l[a + 1] != '-':
        k = float(l[a - 1]) / float(l[a + 1])
    elif x == '*' and l[a + 1] == '-':
        k = -(float(l[a - 1]) * float(l[a + 2]))
    elif x == '/' and l[a + 1] == '-':
        k = -(float(l[a - 1]) / float(l[a + 2]))
    del l[a - 1], l[a - 1], l[a - 1]
    l.insert(a - 1, str(k))
    return l
 
def fun(s):
    l = re.findall('([\d\.]+|/|-|\+|\*)',s)
    sum=0
    while 1:
        if '*' in l and '/' not in l:
            md(l, '*')
        elif '*' not in l and '/' in l:
            md(l, '/')
        elif '*' in l and '/' in l:
            a = l.index('*')
            b = l.index('/')
            if a < b:
                md(l, '*')
            else:
                md(l, '/')
        else:
            if l[0]=='-':
                l[0]=l[0]+l[1]
                del l[1]
            sum += float(l[0])
            for i in range(1, len(l), 2):
                if l[i] == '+' and l[i + 1] != '-':
                    sum += float(l[i + 1])
                elif l[i] == '+' and l[i + 1] == '-':
                    sum -= float(l[i + 2])
                elif l[i] == '-' and l[i + 1] == '-':
                    sum += float(l[i + 2])
                elif l[i] == '-' and l[i + 1] != '-':
                    sum -= float(l[i + 1])
            break
    return sum
def calculate(expression):
    ex=[]
    ans=0
    if '(' not in expression:
        ans=fun(expression)
        return ans
    for i in range(len(expression)):
        if expression[i]=='(':
            ex.append(i) #ex=[6,7]
        elif expression[i]==')': #14
            temp=0
            sub=expression[ex[len(ex)-1]+1:i]
            temp=fun(sub)
            expression=expression[0:ex[len(ex)-1]]+str(temp)+expression[i+1:len(expression)+1]
            ex.pop()
            return calculate(expression)
 
s='1 - 2 * ( (60-30 +(-40/5+3) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
print(1 - 2 * ( (60-30 +(-40/5+3) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ))#1735397.4095238098
s3='3*(4+50)-((100+40)*5/2-3*2*2/4+9)*(((3+4)-4)-4)' #518.0
print(3*(4+50)-((100+40)*5/2-3*2*2/4+9)*(((3+4)-4)-4))
print(calculate(s))#1735397.4095238098
print(calculate(s3))#518.0
