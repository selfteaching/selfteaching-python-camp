#python的str()字符串类型的方法详解https://www.cnblogs.com/gouguoqilinux/p/9114463.html
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
v=text.replace('better','worse')
# 将字符串样本 text ⾥的 better 全部替换成 worse
print(v)
#将单词中包含 ea 的单词剔除
text=v.split()
a='ea'
b=[]
for i in text:
    if i.find(a)<0:
        b.append(i)
print(b) 
#将字⺟进⾏⼤⼩写翻转（将⼤写字⺟转成⼩写，⼩写字⺟转成⼤写）
c= [ j.swapcase() for j in b ]
print(c)
#将所有单词按 a…z 升序排列，并输出结果
print(sorted(c, reverse = False))
