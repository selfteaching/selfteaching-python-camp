a = '''The Zen of Python, by Tim Peters

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
There should be one -- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
print('task1:\n')
a=a.replace('better','worse')
print(a)
print('task2:\n')
b=a.split( )
c=[]
for i in b:
    if i.find('ea')<0:  
      c.append(i)
print(c)
print()

print('task3:\n')
d=" ".join(c)
d=d.swapcase()
print(d)
print()

print('task4:\n')
e=d.split()
e.sort()
print(e)


