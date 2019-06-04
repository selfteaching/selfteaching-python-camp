#定义文本text的内容

text = '''
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

#替换单词
a=text.replace('better','worse')
print(a)

#将非英文字符替换为空格
x=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ').replace('!',' ')

#剔除含有“ea”的单词
b=x.split()
c='ea'#定义c的内容
d=[]#定义d是一个列表
#创建一个循环，检索符合c内容的值，并返回到列表d里，完整语句str.find(str,beg=0,len(string)),x.find(a,1,5)的意思是检索从1开始到第5个字符里是否有a，并返回一个a位置的值。
for e in b:
    if e.find(c)<0:# 如果c='c',那==0代表第一个字母是c，==2代表第3个字母是c，>0代表包含c的单词，<0代表不含c的单词
        d.append(e)
print(d)

#翻转大小写,swapcase语法可以直接实现这一功能。
f=','.join(d)
g=f.swapcase()
print(g)

#单词按照a-z排列
d.sort()
i=','.join(d)
j=i.swapcase()
print(j)