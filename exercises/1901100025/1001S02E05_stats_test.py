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
text_lower = text.lower()
text_split = text_lower.split()
symbols = ',*-.!'
words = []
for word in text_split:
    for symbol in symbols:
        word = word.replace(symbol, '')
    if len(word):
        words.append(word)
text_count ={}
text_set = set(words)
for word in text_set:
    text_count[word] = words.count(word)
print('This is homework 2.2 count words:\n', text_count)
print('This is homework 2.3 sort words:\n', sorted(text_count.items(), key = lambda x: x[1], reverse = True)) 