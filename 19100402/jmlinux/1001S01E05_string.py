stringbefore = '''
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
#------------------better替换worse------------------------
string1=stringbefore.replace("better","worse")

#------------------删除ea------------------------
string2 = string1.split()
string3="ea" 
string4=[]
for i in string2:
    if i.find(string3)<0:
        string4.append(i)
string5=" ".join(string4)  
#-----------------大小翻转-------------------------
string6 = string5.swapcase()
#-----------------a-z排序-------------------------
string7 = string6.replace(","," ").replace("."," ").replace("--"," ").replace("!"," ").replace("*"," ")
string8 = string7.split()
string9 = sorted(string8)
string10 = " ".join(string9)
print(string10)