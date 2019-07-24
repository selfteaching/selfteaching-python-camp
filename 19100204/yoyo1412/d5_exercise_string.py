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
word=text.split()
print(word)
a=0
for i in word:
    if i=='better':
        word[a]='worse'
    a=a+1
a=0
print(word)
for i in word:
    if "ea" in word[a]:
        del word[a]
    a=a+1
a=0
print(word)
for i in word:
    word[a]=word[a].swapcase()
    a=a+1
print(word)
word = sorted(word, key=str.lower)
print(word)
