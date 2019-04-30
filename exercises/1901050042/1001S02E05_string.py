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
Rs_str = text.replace('better','worse')
print(Rs_str)
print('==============第一步完成=============')

RRs_str = Rs_str.split(' ')#利用split切片 利于遍历每个单词

j = ''
for i in RRs_str:
    if 'ea' not in i:#判断每个单词中是否含有‘ea’ 不含有的把它们拼接起来
        j =j+i+' '
print(j)
print('==============第二步完成=============')

print(j.swapcase())

print('==============第三步完成=============')

j= j.split()
j.sort()#排序
print(j)
print('==============第四步完成=============')