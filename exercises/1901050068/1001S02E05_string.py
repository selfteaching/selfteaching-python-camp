test = '''
The Zen of Python,by Tim Peters


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
There should be one-- and preferably only one -- obvious way to do it.
Although never is often better the *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#better全部替换成worse
test= test.replace('better','worse')
print(test)

#包含ea的单词删除
test=test.split()
x='ea'
y=[]
for i in test:
    if i.find(x)<1:
       y.append(i)
print(y)


#大小写转换
a=''
b=a.join(y)
y2=b.swapcase()
print(y2)

#a到z升序排列
c=y2.split()
y3=sorted(c)
print(y3)


