 
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

list1=text.split()
list2=[]
list3=[]
a=len(list1)
while a>0:
    for x in list1:
        list2.append((list1.count(x)))
        list3.append(x)
        i= 0 
        j= 1 
        while i< len(list1):
            j = i + 1
        while j < len(list1):
            if list1[i] == list1[j]:
                del li[j]
                continue
                j = j + 1
            i = i + 1

        
            a=len(list1)
    #list2.append((list1.count(i)))

       # print(list2)
        #print(list3)
       # print(list1)
dict1=dict(zip(list2,list3))
print(dict1)
