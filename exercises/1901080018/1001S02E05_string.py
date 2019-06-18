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
newtext=text.replace('better','worse')
print(newtext)
text1 = newtext.split()
text2 = "ea"
text3 = []
for i in text1:
    if i.find(text2)<0:
        text3.append(i)
text4 = " ".join(text3)
print(text4)
text5 = text4.swapcase()
print(text5)
text6 = text5.replace(","," ").replace("."," ").replace("!"," ").replace("--"," ").replace("*"," ")
text7 = text6.split()
text8 = sorted(text7,key=str.lower)
text9 = " ".join(text8)
print (text9)