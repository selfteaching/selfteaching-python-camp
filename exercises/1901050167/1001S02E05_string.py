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

#better替换成worse
print(text.replace('better','worse'))
#将单词中包含 ea 的单词剔除
y=text.replace('better','worse')
z=y.split()
str1='ea'
str2=[]
for i in z :
    if i.find(str1)< 0:
        str2.append(i)
print(" ".join(str2))
#将第 3 步的结果里的字母进行大小写翻转
a=" ".join(str2)
a=a.swapcase()
print(a)
#将第 4 步的结果里所有单词按 a…z 升序排列列
b=a.split()
b.sort()
print(b)