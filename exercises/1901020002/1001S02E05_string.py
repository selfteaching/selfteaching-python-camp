sample_text = '''
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

#1.2 better替换worse
test = sample_text.replace('better','worse')
print('better全部替换成worse',test)

#1.3 剔除包含ea的单词
words = test.split()
filtered = []
for word in words:
    if word.find('ea') < 0:
        filtered.append(word)
print('剔除包含ea的单词',filtered)

#1.4 大小写翻转
swapcased = [i.swapcase() for i in filtered]
print('大小写翻转',swapcased)

#1.5 升序排列
print('升序排列',sorted(swapcased))
print('降序',sorted(swapcased,reverse=True))