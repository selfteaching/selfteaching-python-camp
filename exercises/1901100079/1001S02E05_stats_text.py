text='''
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
a=text.split() 
#b=list(a) 该方法里会包含各类符号，要先去除
b=[] #定义一个变量的类型为list
c='-,!*.'
for x in a:
    for y in c:
        x=x.replace(y,'')
    if len(x):
        b.append(x)        
print(b)

d={} #把d定义为一个字典
E=set(b) #计数还是回b中计，但是为了减少循环，用set可以把重复元素给省去
for e in E: #对set中这样的元素进行计数
    d[e]=b.count(e) 
print('各单词出现次数：',sorted(d.items(),key=lambda x: x[1],reverse=True))
