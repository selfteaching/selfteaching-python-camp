text = ''' The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! '''

#替换单词
t1=text.replace("better","worse")
 
#print(ti)可以查看结果，t1内容全部better已经替换为worse
 
#剔除ea
list1=t1.split()
list2=[]
str1="ea"
for t1 in list1:
    if str1 not in list1:
        list2.append(t1)
a=[str(i) for i in list2 ]
b=" ".join(a)
 
#字母进行大小写翻转
c=b.swapcase()
d=c.upper()
 
#所有单词按a-z顺序排
e=(d.split(" "))
print(e)
print(sorted(e, key=str.lower))