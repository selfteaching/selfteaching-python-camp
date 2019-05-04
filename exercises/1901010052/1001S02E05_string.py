  
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
# better替换成worse
a=text
b=a.replace('better','worse')
print(b)
#任务2 将上一步结果中将包含ea的单词剔除
c=b.split()
d='ea'
e=[]
for i in c:
    if i.find(d)<0:
        e.append(i) 
print(e)
#任务3 上一步结果大小写转换。
f=a.swapcase()
print(f)
#任务4 将上步操作后的结果所有单词按A-Z顺序排列，并输出结果。
g=e.sort()
print(g)

