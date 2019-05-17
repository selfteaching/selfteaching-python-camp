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
#01 去除标点
t01 = ''.join(i for i in text if i not in "-.,!*")
#02 better 替换成 worse 
t02 = t01.replace('better', 'worse')

#03 从第二部结果中，将单词中包含ea的单词剔除
t03 = t02.split()
print(t03)

for a in t03:
    if "ea" in a:
        print("移除", a)
        t03.remove(a) 
t03=" ".join (t03)
print(t03)

#04 将第3步的结果里面的字母进行大小写翻转
t04=t03.swapcase()
print(t04)


#05 将第4步的结果里所有的单词按照a...z排序并输出结果

t05 = t04.split()
t05.sort()
print(t05)