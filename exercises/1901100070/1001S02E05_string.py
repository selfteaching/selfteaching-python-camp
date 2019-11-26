text = '''
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
1There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
print()
print()
text = text.replace('better', 'worse')
print('老板，better都已经改成worse了\n\n', text, end='\n\n\n')

words = text.split()
filtered = []
for word in words:
    if word.find('ea') == -1:
        filtered.append(word)
print('老板，已经把含有ea的单词都干掉了\n\n', filtered, end='\n\n\n')

swapcased = [i.swapcase() for i in filtered]
print('乾坤大挪移，大的变小，小的变大\n\n', swapcased, end='\n\n\n')

print('列队,从a到z排好哦\n\n', sorted(swapcased))