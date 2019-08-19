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
l1=text.split()
l2=[]
sy=',.*-!'

for l3 in l1:
    for sy2 in sy:
        l3 = l3.replace(sy2,'')
    if len(l3):
        l2.append(l3)
print(l2)

counter={}
words=set (l2)

for word in words:
    counter[word]=l2.count(word)
print (counter ) 

print (sorted(counter.items(),key=lambda x:x[1],reverse=True))
# 重新提交作业