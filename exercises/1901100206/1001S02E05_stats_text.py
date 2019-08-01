text='''
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
text_1 = text.lower().replace(",", "").replace(".", "").replace("-", "").replace("!", "").replace("*", "")
text_2 = text_1.split()

#第零种，未解决方法，原创
#text_3 = list(range(len(text_2)))
#text_4 = zip(text_2, text_3)
#print(dict(text_4))

#第一种解决方法，非原创
#dit = {}
#for key in text_2:
#    dit[key] = dit.get(key, 0) + 1
#print(dit)

#第二种解决方法，半原创
dit = {}
for key in set(text_2):
    if text_2.count(key) > 0:
        dit[key] = text_2.count(key)
print(sorted(dit.items(), key=lambda item:item[1], reverse=True))
