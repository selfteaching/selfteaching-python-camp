#1、创建一个名为d5_exercise_stats_text.py的文件
#2、使用字典（dict）统计字符样本text中各个英文单词出现的次数
#3、示例：{'is': 10, 'better': 9, …}
#4、按照出现的次数从大到小输出所有的单词及出现的次数
#5、只统计英文单词，不包括非英文字符的其他任何符号，如连接符号、空白字符等

text = ''' The Zen of Python, by Tim Peters

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

There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never.

Although never is often better than *right* now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!

'''

text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')#将非英文字符替换为空格
text=text.lower()#将所有英文字符改为小写
text=text.split()#以空格拆分独立的单词
zidian={}
for i in text: #将字符转换为字典
    count=text.count(i)
    r1={i:count}
    zidian.update(r1)
print(zidian)

zidian1=sorted(zidian.items(),key=lambda x:x[1],reverse=True)#按照单词出现次数，从大到小排序
print(zidian1)
