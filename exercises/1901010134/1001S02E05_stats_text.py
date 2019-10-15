text= '''
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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
 
list1 = text.split( )
for i in range(len(list1)): #range(len())计算字符串列表总长度。len()返回值：字符串、列表、字典、元组等元素的长度
    list1[i]= list1[i].strip('*-,.!') #strip()括号里可以指定多个字符模式，顺序无所谓但是只能去除头和尾的
    while ' 'in list1:    #去除空白字符
        list1.remove(' ')
import collections   #引入collections模块
print(collections.Counter(list1))


