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
If the implementation is easy to explain, it's may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
print('This is homework 1.2: replace better to worse\n', text.replace('better', 'worse'))
text_replace = text.replace('better', 'worse')
text_split = text_replace.split()
text_noea = []
for words in text_split:
    if 'ea' not in words:
        text_noea.append(words)
print('This is homework 1.3: remove words with ea\n', text_noea)
text_swapcase = [i.swapcase() for i in text_noea]
print('This is homework 1.4 swapcase\n', text_swapcase)
print('This is homework 1.5 sorted words:\n', sorted(text_swapcase))