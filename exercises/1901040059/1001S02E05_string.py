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
import re
s1=text.replace('better','worse') #用 worse 替换掉 better

s2= s1.split()
s3=[]
for i in s2:
    if 'ea' not in i:
        s3.append(i)
s4=''.join(s3)
s4=s4.swapcase()

s3.sort()
print(s3)