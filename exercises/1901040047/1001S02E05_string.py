t = '''
"The Zen of Python, by Tim Peters
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
Namespaces are one honking great idea -- let's do more of those!"

'''

t=t.replace("better","worse")           #把上面段落里的"better"全部替换为"worse"
print(t)

t=t.swapcase()                          #把上面文字的大小写全部对换
print(t)


t=t.replace(',','').replace('.','').replace('!','').replace('*','').replace('--','')     #把标点符号去掉
t=t.split()    #把上面文字变成字符串
x='EA'         #上面的文字已大小写转换
y=[]           #列表
for i in t:
    if i.find(x)<1:#搜索字符串中含有“EA”的单词并删除
        y.append(i)   #把除去含有“EA”外的单词放进列表
print(y)
y.sort()    #排序
print(y)

