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
str1=text.replace('better','worse')
#print(str1)
list1=str1.split()#转换为列表
#print(list1)
list2=[]
for i in list1:#遍历列表
        if 'ea' not in i: 
                list2.append(i)#去除'ea'的列表
                print(list2)
list3=[]
for i in list2:
        if i.isupper():
                list3.append(i.lower())
        elif i.islower():
                list3.append(i.upper())  #未完？？？
list3.sort()
print(list3)#a到z升序排列

