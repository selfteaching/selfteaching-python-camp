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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
print('将字符串串样本 text ⾥里里的 better 全部替换成 worse')
print(text.replace('better','worse'))

print()
print('从第 2 步的结果⾥，将单词中包含 ea 的单词剔除')
text1=text.replace('better','worse')
text2=text1.split()   # string 转为 list
text3=[]
for letter in text2:
    if 'ea' not in letter:
        text3.append(letter)
print(text3)


print()
print('将第 3 步的结果⾥的字⺟进⾏⼤⼩写翻转（将⼤写字母转成⼩写，⼩写字母转成大写）')
str=' '
text4=str.join(text3)   # list 转为 string
print(text4.swapcase())


print()
print('将第 4 步的结果⾥所有单词按 a…z 升序排列列，并输出结果')
text5=text4.swapcase()
text6=text5.split()     # string 转为 list
text6.sort(key=lambda x:x.lower())
print(text6)