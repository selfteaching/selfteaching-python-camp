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

textList = text.split()
for i in range(len(textList)):
    textList[i] = textList[i].strip(',*-.!')
newList = dict.fromkeys(textList, 0)

for i in range(len(textList)):
    if textList[i] in newList.keys():
        # print('---------------')
        newList[textList[i]] += 1
sorted_x = dict(sorted(newList.items(), key=lambda kv: kv[1], reverse=True))
print(sorted_x)
