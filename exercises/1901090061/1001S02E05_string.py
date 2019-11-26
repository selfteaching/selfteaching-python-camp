text = '''
The Zen Of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than implicit.
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
If the implementation is easy to explain, it may be a good ieda.
Namespaces are one honking great idea -- let's do more of those!
'''
text = text.replace('better','worse')
print(text)
text_list_1 = text.split()
text_list_2 = []
for x in text_list_1:
    if 'ea' not in x:
        text_list_2.append(x)
print(text_list_2)
text_1 = ' '.join(text_list_2)
text_2 = text_1.swapcase()
print(text_2)
text_list_3 = text_2.split()
print('按字母升序排列：')
print(sorted(text_list_3))