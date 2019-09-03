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
print('better' in text)

print(text.replace('better', 'worse'))
text_two = text.replace('better', 'worse')

# 剔除test里面包含ea的单词。
# 我一直想的思路是：找到一个可以用的method，直接删掉，结果是一直没找到......
# 出现这种错误思路的原因是因为重复次数太少，没有想出来或者说记得String是Immutable
# 正确思路是将String转换成List，找到不含有ea的单词，再重新生成个List

y = text_two.split()

temp1="ea"
list2=[]
for i in y:
    if i.find(temp1) == -1:
        list2.append(i)
print(list2)
print()

string2 = str(list2)
print(string2.swapcase())
print()

print(sorted(y, key=str.lower))