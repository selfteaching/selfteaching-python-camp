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
d={}#新建字典集合
t1=text.split()#将字符串转化为列表
set1=set(t1)#将列表转为集合，去除列表中的重复字符
t2=list(set1)#将集合转为没有重复字符的列表
for x in range(len(t2)):#len函数能够返回列表的个数，x历遍列表中的元素
    d[t2[x]]=0#初始值为零
    for y in range(len(t1)):#y历遍t1
        if t2[x]==t1[y]:#如果x=y
            d[t2[x]] += 1#则x元素增加1
print(d)

d1=sorted(d.items(),key=lambda item:item[1],reverse=True)#items()函数将字典转化为元组，key lambda item：item[1]表示选第二个元素做比较，reverse表示降序
print(d1)

d2=str(d1)
print(d2)

#清楚非单词字符
word=[]
s=',.*-!'
for i in t1:
    for j in s:
        i=i.replace(j,'')
    if len(i):
        word.append(i)
print(word)

#统计单词数
counter={}
w1=set(word)
w2=list(w1)
for a in range(len(w2)):
    counter[w2[a]]=0
    for b in range(len(word)):
        if w2[a]==word[b]:
           
            counter[w2[a]]+=1
print(counter)
print('只包含英文单词的统计')
counter1=sorted(counter.items(),key=lambda item:item[1],reverse=True)#items()函数将字典转化为元组，key lambda item：item[1]表示选第二个元素做比较，reverse表示降序
print(counter1)

print('尝试教练的方法')
for a in w2:
    counter[a]=word.count(a)#字典中count 函数能够统计元素的数量，通过等号赋值给元素
print(counter)