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
text2=text.replace("better","worse")
print(text2)

#把text2按行切割成列表
n1=text2.splitlines()
for line in n1:
    n2=line.split(" ")
    for word in n2:
        if "ea" in word:
            text3=text2.replace(word,"")
print(text3)

text4=text3.swapcase()
print(text4)

n3=text4.replace("\n","").replace("."," ").replace("!","").replace("--","").replace("*","")
text5=n3.split(" ")
text5.sort(key=str.lower)
print(text5)