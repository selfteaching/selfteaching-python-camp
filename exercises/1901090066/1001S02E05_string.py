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
#替换
text1=text.replace("better", "worse")
#删除含ea的单词
words=text1.split()
m=[]
for word in words:
   if 'ea' not in word:
       m.append(word)
text3=' '.join(m)
#大小写转换
text4=text3.swapcase()
#单词排序
str=text4.split()
str1=sorted(str)
text5=' '.join(str1)
print(text5)
