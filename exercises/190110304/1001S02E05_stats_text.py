
text=('''
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
Namespaces are one honking great idea -- let's do more of those!''')
text1=text.split()#将字符串转换成列表
text2={}   #创建字典
for i in text1: #for是发起循环的关键词；i in text1是循环规则，i是依次得到txet1列表中的各个值，然后按照索引顺序循环下去，直到最后一个
    if i in text2:
        text2[i]=text2[i]+1 #统计单词出现的次数
    else:
        text2[i]=1
print(text2)

