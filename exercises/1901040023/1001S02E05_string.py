 
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
t = text.replace('better','worse')
print(t)

textlist1 = t.split()   
str1 = [] 
str2 = 'ea'
for i in textlist1: 
    if str2 not in i:
        str1.append(i) 
print(textlist1)


textlist2 = [] 
for i in textlist1:
    i = i.swapcase()       
    textlist2.append(i)
print(textlist2)

textlist2.sort() 
print(textlist2) 