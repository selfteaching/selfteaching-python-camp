sample ="""
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
"""


# 1.将字符串样本里的 better 合部替换成 worse
# str.replace(old,new,count)
text = sample.replace('better', 'worse')
print('\n将字符串样本里的better全部替换成worse ==>', text)

# 2.将单词中包含 ea 的单词删除
words = text.split()
filtered = []
for word in words:
    if word.find('ea') < 0:
        filtered.append(word)
print('\n将单词中包含 ea 的单词删除 ==>',filtered)

# 3.进行大小写翻转
swapcased = [i.swapcase() for i in filtered]
print('\n进行大小写翻转==>',swapcased)

# 4.单词按 a_z 升序排列
print('\n单词按 a_z 升序排列 ==>',sorted(swapcased))