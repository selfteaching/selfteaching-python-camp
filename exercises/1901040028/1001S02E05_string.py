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
t1=text.replace("better","worse")#better替换为worse
t2=t1.split()
t3=[]
for a in t2:
    if 'ea' not in a:
        t3.append(a)              #将包含ea的单词删除

t4=(' '.join(t3))
t5=t4.swapcase()                  #将所有字符中小写字母转换成大写字母
print(sorted(t5.split(), key=str.lower))#将列表中的单词按首字母升序排列)