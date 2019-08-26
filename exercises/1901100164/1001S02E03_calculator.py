#今天的作业是写一个计算器。需要满足加减乘除几个功能

#第一步：首先要设定三个变量，也就是第一个数字，运算符和第二个数字
#变量通常用小写lowerc ase和下划线的形式表示，并且给这三个变量赋值=，需要用到内置函数input
operator=input('请输入运算符（+、—、*、/）')
first_number=input('请输入第一个数字：')
second_number=input('请输入第二个数字：')

#第二步：要做type casting，也就是转换数据类型，input返回的类型是 字符串 string。需要被转化成 integer。
#并且赋值给两个变量 a和b
a=int(first_number)
b=int(second_number)

#第三步：方便起见，用print函数将以上操作打印出来。看一下数据类型。
print('operator',operator,type(operator))# 注意字符需要用引号标注，且必须是英文格式下才行。只有单引号里面的内容才是字符。
print('first_number',first_number,type(a))
print('second_number',second_number,type(b))
#试运行了一下，没问题。operator是字符串，a和b是int整数。

#第四步：写control flow 流程控制 ，需要用到if statement ，elif statemet，else statement
if operator == '+': #if结尾没加引号，导致一直出现error，对照着视频的示例看了半天，才发现要加引号，结果又加的中文引号，还是不对。后来终于改对了啊！！！！
    print(a,'+',b,'=',a + b)#这一行写了半天，哭，不是少逗号，就是少引号。一定要注意区分字符串和变量
elif operator == '-':
    print(a,'-',b,'=',a - b)
elif operator == '*':
    print(a,'*',b,'=',a * b)
elif operator == '/':
    print(a,'/',b,'=',a / b)
else:
    print('无效的运算符')
#rase valueError
