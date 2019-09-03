text='''

The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
print(text.replace("better","worse"))

text_list = text.split()

x = []

for i in text_list:
    if i.find("ea")<0:
        x.append(i)

y=" ".join(x)
print ("剔除含有ea的词: ", y)

z= y.swapcase()
print(z)

z1 = z.split()
print(sorted(z1))

z2=sorted(z1)
print(" ".join(z2))
