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
# 1.将better 改成 worse。
t1 = text.replace('better', 'worse')
print(t1)

# 2.将单词中包含ea的单词剔除。
t2 = t1.split()
x = 'ea'
y = []
for i in t2:
    if i.find(x) < 1:
        y.append(i)
print(y)

# 将字母进行大小写翻转。
t3 = " ".join(y) # 将列表转换成字符串，因为swapcase只能用于字符串的大小写转换，不能用于list
t4 = t3.swapcase()
print(t4)

# 将所有单词按a...z升序排列
t5 = t4.split() # 直接升序排列字符串时会报错，这里需要将字符串进行分隔拆分成list
                # 如果没有给 str.split() 传递参数，那么默认为用 None 分割（各种空白，比如，\t 和 \r 都被当作 None）
#print(t5)
v = sorted(t5)
print(v)
