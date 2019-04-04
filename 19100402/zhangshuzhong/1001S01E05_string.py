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
text2=text1.replace('ea','')#删除'ea'，相当于用于个空元素替换'ea‘
print(text2)
text3=text2.swapcase()#str.swapcase()函数用于将字符串中的字母进行大小写替换
print(text3)

#将字符串中的标点符号去掉
symbol = ",.!-*"
for str in symbol:
    text3= text3.replace(str,'')
print(text3)

#split()函数，针对制定分割符号将字符串进行切片，并返回分割后的字符串列表
text4=text3.split()#这里制定的分割符号是''，这里与上面替换标点符号时候所替换的符号相对
print(sorted(text4))#列表可以直接用sorted()函数排序