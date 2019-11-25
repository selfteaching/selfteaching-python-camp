text='''
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
#1 将字符串样本 text 里的 better 全部替换成 worse
string = text.replace('better','worse')
#2 从第2步第结果里，将单词中包含 ea 的单词剔除
s=string.split() #str.split()分割字符串，默认以空格进行分割。【未去掉标点】
i=[]
for j in s:
    if 'ea' not in j:
        i.append(j)   #将 j 添加到序列的末尾
    else:
        continue

n=[]
for j in i:
    m = j.swapcase()  #大小写翻转
    n.append(m)
n.sort()  #结果里所有单词按a...z升序排序
print(n)