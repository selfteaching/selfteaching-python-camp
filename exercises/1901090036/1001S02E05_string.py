text = ''' 
The zen of python,bu Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special case aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless ecplicitly silences.
In the face of ambxiguity,refuse the temptation to guess.
There should be one-- and preferably only one--obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain,it's a bad idea.
If the inplementation is easy to explain,it may be a good idea.
Namespaces are one honking great idea--let's do more of those!'''
print(text.replace('better','worse'))

x=text.replace('*','').replace('--','').replace('9','')

y=x.split() #split就是将文本中的单词转化为一个个元素
str1="ea"
str2=[]
for i in y:
    if str1 not in i:
        str2.append(i)
print(str2)

str3=(' '.join(str2))
print(str3)

o=text.swapcase()
print(o)

str2.sort()
print(str2)