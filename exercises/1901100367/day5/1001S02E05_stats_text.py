text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
 Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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
#print (f'{text}')
#text.capitalize()
#在一串字符串中，空格也算是一个字符串。如果字符串的开头是一个空格，此时我们会发现capitalize()方法返回的字符串全是小写，这是因为空格没有大小写之分，空格在第一个位置，其它字符串自然全是小写喽
#text.capitalize()
#print(f'{text.capitalize()}')
#print(text)

#print (text.count('ea'))
#better 字符串出现了8次
#1创建一个空字典用dict表示
dict={}

#2把字符串中的非英文字符替换掉
text2=text.replace('.','').replace('!','').replace('*','').replace('--','').replace(',','')
#print(text2)

#print(text.count(is))

#3 把text2字符串裂解
text3=text2.split()
#print(text3)


#4统计词频并转换为字典模式
for x in text3:
        dict[x]=text3.count(x)


#print (dict)

#5把字典按照单词出现的次数从大到小进行排列
#sorted函数的使用方法见网址：https://www.cnblogs.com/dylan-wu/p/6041465.html
dict=sorted(dict.items(),key=lambda item:item[1],reverse=True)      
print (dict)



