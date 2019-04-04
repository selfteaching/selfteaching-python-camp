# String process

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
There should be one -- and preferably only one -- obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# Replace all better to worse
text_worse=text.replace('better','worse')  

# Delete all word containing ea

text_del = text_worse.split()

text_len = len(text_del)

index = []

for test_data in text_del:
    if 'ea' in test_data:
        text_del.remove(test_data)


# revers word 

text_del_len = len(text_del)
for i in range(text_del_len):
    text_del[i] = text_del[i].swapcase()


# sort
text_del.sort()

print(text_del)
