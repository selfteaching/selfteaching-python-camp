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
# better 变成 worse
ss = text.replace('better','worst')
#print(ss,'\n')


#剔除包含ea的单词
a = ss.split()  #分割text文本
for i,v in enumerate (a) :  #enumerate → 表示数组的具体位置和对应的值
    if "ea" in a[i]:#a[i]  找数组当中具体的位置
       del a[i] #剔除数组当中包含ea的单词，而不是局部变量所显示的值。
#print(a,'\n\n')

#字⺟⼤⼩写翻转
b = [y.swapcase() for y in a]#使用swapcase 进行大小写转换
#print(b,'\n\n')

#使用sort()     单词按 a…z 升序排列
b.sort()
print(b)
