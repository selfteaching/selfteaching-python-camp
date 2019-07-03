#1. 创建⼀一个名为 1001S02E05_stats_text.py 的⽂文件

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
#2. 使⽤用字典（dict）统计字符串串样本 text 中各个英⽂文单词出现的次数。示例例： {'is': 10,'better': 9, …}
#把单词分开，标点符号去掉
text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
text=text.lower()
text=text.split()
zidian={}
for i in text: #将字符转换为字典
    count=text.count(i)
    r1={i:count}
    zidian.update(r1)
print(zidian)
#3. 按照出现次数从⼤大到⼩小输出所有的单词及出现的次数
zidian1=sorted(zidian.items(),key=lambda x:x[1],reverse=True)#按照单词出现次数，从大到小排序
# lambda 形参列表 : 函数返回值表达式语句
#下面是个Lambda表达式的例子：
#li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
#li=sorted(li, key=lambda x:x["age"])
#print(li)
#如果不用Lambda表达式，而要写成常规的函数，那么需要这么写：
#!/usr/bin/envpython
#def comp(x):
 #   return x["age"]
#li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
#li=sorted(li, key=comp)
#print(li)


#由 dict.keys(), dict.values() 和 dict.items() 所返回的对象是 视图对象。 该对象提供字典条目的一个动态视图，这意味着当字典改变时，视图也会相应改变。
print(zidian1)
#4. 只统计英⽂文单词，不不包括⾮非英⽂文字符的其他任何符号，如连接符号、空⽩白字符等
