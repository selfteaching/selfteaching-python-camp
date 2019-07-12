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


list1=text.split('')
for i in range(len(list1)):
    list1[i]=list1[i].strip(',*-.!,.\n:,,'',''')


set1=set(list1)
list2=list(set1)

dir1={}
for x in range(len(list2)):
    dir1[list2[x]]=0
    for y in range(len(list1)):
        if list2[x]==list1[y]:
            dir1[list2[x]]+=1
print(dir1)

dir2 = sorted(dir1.items(),key = lambda x:x[1],reverse=True)
print(dir2)