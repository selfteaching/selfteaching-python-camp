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

import string

replace_text = text.replace("better","worse")
# print(replace_text)

split_text = text.split()
print(split_text)

except_text = ""
for words in split_text:
	if "ea" in words:
		continue
	else:
		except_text = except_text + " " + words

print(except_text)


reverse_text = text.swapcase()
print(reverse_text)

replace_text = text.replace('--','').replace(',','').replace('.','').replace('*','').replace('!','')
split_text = replace_text.split()

split_text.sort()
print(split_text)



