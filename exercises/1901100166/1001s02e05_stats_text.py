a = '''
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

#1.使用字典dict类型统计单词出现次数

A=a.split()   #字符串分割成list
B=[]   #定义新的list型变量，储存处理后的单词
C=',.*-!'  #选出样本中要剔除的非单词符号

for AA in A:  #遍历一遍要剔除的符号
    for CC in C:  #逐个替换字符号，用''是为了同时剔除符号所占位置
        AA=AA.replace(CC,'')  #剔除字符后如果AA的长度不为0，则算正常单词
    if len(AA):
        B.append(AA)

print('纯单词==>',B)

counter={}  #初始化一个dict类型的变量，来存放单词出现次数

B_set=set(B)  #set(集合)使重复的元素只出现1次，减少在for in 里的循环次数

for BB in B_set:
    counter[BB]=B.count(BB)  #BB是对单词的项进行赋值，表明单词出现多少次

print('单词次数==>',counter)

#2.
print('从大到小==>',sorted(counter.items(),key=lambda x:x[1],reverse=True))  

#E.items() 是一个字典的方法，会返回一个列表即含（key，value）的 元组，我们是在对此列表排序，
# key指单词，value指单词出现的次数，lambda函数取第一项