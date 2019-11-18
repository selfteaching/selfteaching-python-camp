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
print (text.replace('better','worse')) 

text1=text.replace('better','worse')
text2=text1.split()
text3=[]

for x in text2:
    if 'ea' not in x:
        text3.append(x)
print(text3)

text4=(''.join(text3))
text5=''
text5=text4.swapcase()
print(text5)

import re
text=re.split(r"\W+",text5)
text.sort()
while '' in text:  
    text.remove('')
print(text)
    