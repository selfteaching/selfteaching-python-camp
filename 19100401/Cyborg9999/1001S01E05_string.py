text = '''
The Zen of python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases arent't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced
In the face of ambxiguity,refuse the temptation to guess
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch
If the implementation is hard to explain,it's a bad idea
If the implementation is easy to explain,it's may be a good idea.
Namespaces are one honking great idea --let's do more of those!
'''

lst=text.split()
str1="ea"
str2=[]
for i in lst:
    if i.find(str1) < 0:#find的意思是如果没有找到，返回值为-1
        str2.append(i)
print(str2)
#如果还不是很清楚，可以运行如下代码，前两个的意思应该是找出索引4、5的内容，没有找到，因此返回-1，另外三个，得到的是：0、1、2
#print('123'.find('4'), '123'.find('5'), '123'.find('1'), '123'.find('2'), '123'.find('3'))

text=text.replace('better','worse')
print(text)

text=text.swapcase()
print(text)

str2.sort()
print(str2)