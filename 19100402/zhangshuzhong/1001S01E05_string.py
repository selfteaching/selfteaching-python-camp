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
text1=text.replace('better','worse')#使用str.replace()函数，主要用于字符串中元素的替换，用后一个元素替换前一个元素
print(text1)

#将字符串中的标点符号去掉
symbol = ",.!-*"
for str in symbol:
    text1= text1.replace(str,'')
print(text1)

#split()函数，针对制定分割符号将字符串进行切片，并返回分割后的字符串列表
text2=text1.split()#这里制定的分割符号是''，这里与上面替换标点符号时候所替换的符号相对


text3=[]#新建一个空的列表
for i in text2:
    if i.find('ea')<0:#逐一寻找“ea”,如果该单词中包含ea那么find()函数会输出其位置，如果没有那么结果会为-1（及小于0）
        text3.append(i)#如果结果小于0，那么就将这个单词添加到新的列表中，开始下一个循环
print(text3)

str1=" ".join(text3)#join()是将列表转换为字符串，每个单词之间我使用空格作为间隔
str2=str1.swapcase()#str.swapcase()函数用于将字符串中的字母进行大小写替换
print(str2)

print(sorted(str2.split( )))#先使用split()函数将字符串转化为列表，这里的分割符号是空格。然后再使用sorted()函数对列表排序