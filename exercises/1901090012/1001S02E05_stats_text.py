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

d={}
t1=text.split()
set1=set(t1)
t2=list(set(t1))
for x in range(len(t2)):
    d[t2[x]]=0
    for y in range(len(t1)):
        if t2[x]==t1[y]:
            d[t2[x]]+=1
print(d)


d1 = sorted(d.items(),key=lambda item:item[1],reverse=True)
print(d1)


d2=str(d1)
print(d2)

word=[]
s=',.*-!'
for i in t1:
    for j in s:
        i=i.replace(j,'')
    if len(i):
        word.append(i)
    print(word)    
counter={}
w1=set(word)
w2=list(w1)
for a in range(len(w2)):
    counter[w2[a]]=0
    for b in range(len(word)):
        if w2[a]==word[b]:
            counter[w2[a]]+=1
print(counter)

print('只包含英语单词的统计')
counter1=sorted(counter.items(),key=lambda item:item[1],reverse=True)
print(counter1)

print('尝试教练的方法')
for a in w2:
    counter[a]=word.count(a)
print(counter)    
















