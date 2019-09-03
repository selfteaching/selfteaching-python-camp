#day5 homework
#复制文本
#把better替换为worse
#剔除包含ea的单词
#大小写翻转
#按照a-z升序排列

#复制文本
 
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

#把better替换成worse
t1 = text.replace('better','worse')

#删除包含ea的单词
t2 = t1.split()  #把字符串变成list
t3 = [x for x in t2 if 'ea' not in x]

#大小写翻转
t4 = " ".join(t3) #把list变回字符串
t5 = t4.swapcase()

#按照a-z升序排列
t6 = t5.split() #变回list
t6.sort( )
print(t6)