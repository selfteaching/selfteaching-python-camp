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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#将文本中的better用worse替换掉
text = text.replace('better','worse')
print(text)

#将单词中包含 ea 的单词剔除
list = text.split()
str1 = 'ea'
str2 = []
for i in list:
    if i.find(str1)<0:
        str2.append(i)
print(str2)

#将字母大小写反转
text1 = ''
for i in str2:
    text1 =text1 + ' ' + i
print(text1)
text = text1.swapcase()
print(text)

#所有单词按 a…z 升序排列
list = text.split()
list.sort()
print(list)

#split（）方法默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等，所以未对特殊符号做处理，所以提取出的单词中存在“--”，“.”等的情况，这是需要优化的点