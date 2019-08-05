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
text2=text.replace('better','worse')
print(text2)

text3=text.split()
newtext=[]
for word in text3 :
    if word.find('ea')<0:
        newtext.append(word)
print(newtext)

text4 =' '.join(newtext)  # 到这一步是可以打印出字符串的
text5=str(text4).swapcase()  # 这一步的method已经不能自动显示了，swapacase是我自己手动打上去的
print(text5)  # 报错 是因为调用method没有用（）

t6=text5.split()
print(t6)
# t6=[str(i).swapcase() for i in newtext]
# print(t6)

print(sorted(t6))

print(sorted(t6,reverse=True))