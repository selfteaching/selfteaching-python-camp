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
#将text中better置换为worse
a = text.replace('better','worse')
#将a中含“ea”的单词删除
list0 = ''
list1 = ''
list2 = ''
list1 = list0.join(a)  
import re
list2 = re.split(r"(\W+)",list1)   
for i in list2:  
    if 'ea' in i:   
        list2.remove(i) 
#将list2中大小写翻转
list3 = ''
list4 = ''
list5 = ''
list4 = list3.join(list2) 
list5 = list4.swapcase()   
#将结果单词按a...z升序排列
b = re.split(r"\W+",list5)   
b.sort()    
while '' in b:   
    b.remove('')
    print(b)