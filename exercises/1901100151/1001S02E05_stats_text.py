# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

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

print()
print("将字符串串样本text⾥里里的better全部替换成worse:\n")
# print("better" in text)
# print(text.count('better'))
# print("text.replace('better','worse'):\n")
print(text.replace('better','worse'))
text1 = text.replace('better','worse')
# print(text1.count('worse'))
print()

print("将单词中包含 ea 的单词剔除:\n")
# print(text1.count('ea'))
a = text1.split()
# print(a)
b = []
text2 = []
for c in a:
    if c.find('ea') > 0:
        b.append(c)
    else:
         text2.append(c)
# print(b)
print(text2)
print()

print("将text2中的字母进行大小写翻转:\n")
# print(text.lower())
# print(text.upper())
# print(text.swapcase())
# print(text.casefold())
# x = "an"
# y = "An"
# print(x.swapcase(),y.swapcase())
text3 = [i.swapcase() for i in text2]
print(text3)
print()

print("将text3中所有单词按a...z升序排列列:\n")
text4 = sorted(text3)
print(text4)
print()

# error:
# print()
# print("将字符串串样本text⾥里里的better全部替换成worse:\n")
    # print(text.replace('better','worse'))
    # text1 = text.replace('better','worse')
# print()