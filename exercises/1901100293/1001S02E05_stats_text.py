text ='''
The Zen of Python, by Tim Peters.
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
a=text.replace('.',' ').replace('\n',' ')\
    .replace('-',' ').replace('!',' ')\
        .replace(',',' ').replace('*','')   #去除标点符号
a=a.split() #转化为list类型
b=set(a)    #b赋值为a的元素集，清除了重复项
di={}   #定义di为字典
for c in b: #遍历元素集b中的元素c
    d=a.count(c)    #计算元素c在a中出现的次数d
    di[c]=d #把每一对键c/值d加到di集里面去
#到这里di已经是个包含所有单词出现次数的字典
p=sorted(di.items(),key=lambda x:x[1],reverse=True) 
#sorted为排序
#di.items()表示遍历字典并输出成包含元组的列表p
#key=lambda为固定表达，lambda是一个参数
#x:x[1]表示在列表p中，每个元组x的第二个元素x[1],第一个为x[0]
#reverse=ture为反向排序，不写则为正向排序
#综上就是把字典di输出成一个由元组构成的list并且按照每个元组中的第二个元素从大到小排序
print(p)