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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#根据字符串先将 空白字符分割成list，要调用str类型
dictionary=text.split()
#定义一个新的list变量，存储处理过的单词
b=[]
a=',.*!-'
for dictionaries in dictionary:
#遍历一遍需要剔除的非单词符号
    for aa in a :
          dictionaries=dictionaries.replace(a,'')
    if len(dictionaries):
            b.append(dictionaries)
print(b)
#初始化一个dict(字典)类型的变量，用来存放单词出现的字数
counter={}
#set(集合)类型可以去掉列表里面的重复元素，可以在for...in里面减少重复次数
b_set=set(b)
for c in b_set:
        counter[c]=b.count(c)
print('英语单词出现的次数==>',counter)
#按照出现次数从⼤到⼩输出所有的单词及出现的次数
# 内置函数sorted的参数key表示按元素那一项的值进行排序
# dict类型的counter的items方法会返回一个 包含 相应项(key,value)的元组列表
# print('counter.items()==>',counter.items())       
print('按照出现次数从⼤到⼩输出所有的单词及出现的次数==>',sorted(counter.items(),key=lambda x:x[1],reverse=True))