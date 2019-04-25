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

# 参考 https://stackoverflow.com/questions/3496518/python-using-a-dictionary-to-count-the-items-in-a-list
# https://docs.python.org/3/library/collections.html#collections.Counter
text2 = text.replace('--',' ').replace(',',' ').replace('!',' ').replace(':',' ')
y = text2.split()

i = y
d = {x:i.count(x) for x in i}
print(d)

print()
d1 = sorted(d.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从大到小排序
print(d1)