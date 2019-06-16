t = '''
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
print("Task 1: replace \"better\" with \"worse\".")
t1 = t.replace("better","worse")
print(t1)

print("Task 2: delete words contain \'ea\'")
t2 = ascii(t1)
t2 = t2.replace('Peters','Peters.')
t2 = t2.replace('\\n',"")
t2 = t2.replace(' -- '," ")
t2 = t2.replace("."," ")
t2 = t2.replace('\'',"")
t2 = t2.replace('\"',"")
t2 = t2.replace('-',"")
new_list = t2.split(' ')
new_list1 = list()
for i in new_list:
    if i.find('ea') <0:
        new_list1.append(i)
print(new_list1)

print("\nTask 3: swapcase all the words")
new_list2 = list()
for i in new_list1:
    new_list2.append(i.swapcase())
print(new_list2)
    
print("\nTask 4: sort from a to z")
new_list3 = sorted(new_list2)
print(new_list3)