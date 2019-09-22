#1.打印的时候打印一个结果；2.这个结果是我输入一个数值，我输入加减乘除，我输入另一个数值运算后出来的
#问题1.我怎么能输入数值；2.怎么输入加减乘除；
#用input输入数值，输入的时候这个数值是会变化的，所以得是个变量；而且计算完之后还得有一个按键返回到最初的样子，便于再输入

a=input('请输入一个数值:')#字符串用''
b=input('请输入一个数值:')
c=input('请输入运算符号(+,-,*,/,):')#到这里等号两侧的东西应该都万事了
#如果输入的值类型不同也不行，运算不了，所以需要转换数值类型
d=int(a)
e=int(b)
if c=='+':#z这里要注意  1.等号是用==  2.语言块中的第一行要加个：
   n=(d+e)
   print(n)
elif c=='-':
   n=(d-e)
   print(n)
elif c=='*':
    n=(d*e)
    print(n)
elif c=='/':
    n=(d/e)
    print(n)
#程序运行是按照从上到下的顺序进行的，所以你想让他先显示啥，就先写啥。当然准备工作是要在先显示的东西之前写的。
#有点乱，还是缕顺一下吧，过程：输入一个数字，一个运算符号，一个数字；然后打印这个式子的结果

txt = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
txt2=txt.replace("better","worse")
print(txt2)