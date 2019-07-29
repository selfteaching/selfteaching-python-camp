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


# 1、将字符串串样本text⾥里里的better全部替换成worse
text = text.replace('better','worse')
print('将字符串里的better全部替换为worse：',text)

# 从第 1 步的结果⾥里里，将单词中包含 ea 的单词剔除
words = text.split()  # 切成一个列表,如果写text.split（' '）的话，换行符号会保留
print(words)

filtered = [] #用来存放单词
for word in words:  # 遍历这个列表,把含有 ea 的东西剔除掉
    if word.find('ea')< 0:
        filtered.append(word)
print('将单词中包含ea的单词剔除',filtered)

# 将第3步的结果⾥的字⺟进⾏大小写翻转
swapcased = [i.swapcase() for i in filtered]
print(swapcased)

# 将第4步的结果⾥里里所有单词按a...z升序排列列，并输出结果

print(sorted(swapcased))

# 将字符串串样本text⾥里里的better全部替换成worse


print('better' in text)
text = text.replace('better','worse')
print(text)

print('1=======================')

# 从第 2 步的结果⾥里里，将单词中包含 ea 的单词剔除
text = text.split()  # 切成一个列表,如果写text.split（' '）的话，换行符号会保留
print(text)

print('2=======================')



list1 = []
for i in text:  # 遍历这个列表,把含有 ea 的东西剔除掉
    if 'ea' not in i:
        list1.append(i)

print(list1)

print('3=======================')

# 将第3步的结果⾥的字⺟进⾏大小写翻转

text2 = []
for i in list1:
    i.strip()
    text2.append(str(i).swapcase())

print(text2)
print('4=======================')

# 将第4步的结果⾥里里所有单词按a...z升序排列列，并输出结果
text2.sort()
print(text2)

print('5=======================')

