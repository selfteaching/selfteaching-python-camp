text='''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than implicit.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the tules.
Although praticality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one -- and preferably only one -- bovious way to do 
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now .
If the implementation is hard to explain, it's bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

#使⽤用字典(dict)统计字符串串样本text中各个英⽂文单词出现的次数
#只统计英文单词，所以要把test中的其它不是英文单词的东西去掉。这里用空格去替换掉桃运点符号。

s1=text.replace(',','').replace('.','').replace('--','').replace('!','').replace('*','')  #去除标点符号（没有找到更好的办法，如果文本格式很多怎么办？）
s1=text.lower()   #把单词全部变为小写
s1=text.split()   #把字符串分割成单个单词列表

dict={}          #用花括号创建一个字典
for i in s1:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
text_1 = sorted(dict.items(), key=lambda y: y[1], reverse=True)   #key为排序依据，y【0】为key，1为y，这里不太懂，reverse为true时降序。

print(text_1)






