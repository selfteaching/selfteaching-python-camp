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

text=text.replace(',','').replace('.','').replace('--','').replace('!','').replace('*','')  #去除标点符号（没有找到更好的办法，如果文本格式很多怎么办？）
text=text.lower()   #把单词全部变为小写
text=text.split()   #把字符串分割成单个单词列表

dict={}
for x in text:
    if x in dict:
        dict[x]=dict[x]+1
    else:
        dict[x]=1
text_1 = sorted(dict.items(), key=lambda y: y[1], reverse=True)   #key为排序依据，y【0】为key，1为y，这里不太懂，reverse为true时降序。

print(text_1)


