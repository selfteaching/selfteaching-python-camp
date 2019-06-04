s= """
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
"""
#第一步
s=s.replace('better', 'worse') # better 替换成 worse
print(s)

#第二步
s=s.swapcase()
print(s)

#第三步
s=s.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')#把各种符号替换成空格
s=s.split()#用空格把文章拆分为独立的单词
s1="ea"  #剔除包含ea的单词
s2=[]
for i in s:
    if i.find(s1)<1:
        s2.append(i)
print(s2)
print()

#第四步
s2.sort()#将所有单词排序
print(s2)