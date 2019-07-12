import re
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

word_dict = {}
for row in text.splitlines(True):
    for word in row.split(' '):
        match_obj = re.search('([a-zA-Z]+)', word)
        if match_obj is not None:
            w = match_obj.group(1)
            w = w.lower();
            if w in word_dict:
                word_dict[w] += 1
            else:
                word_dict[w] = 1

# 参考：https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
for key, value in sorted(word_dict.items(), key=lambda item: item[1], reverse=True):
    print("{}: {}".format(key, value))