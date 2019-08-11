text='''
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
#所有better替换成worse
text2=text.replace ('better', 'worse')
print(text2)   

#去掉所有包含ea的单词
text3=[]                                   
for word in text2.split():                          
       if word.find('ea')<0:
               text3.append(word)
str = ' '        
print(str.join(text3))

#翻转大小写
text4 = text.swapcase()
print(text4)

#字母排序
print(sorted(text3, reverse=False))


