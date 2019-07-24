# this is d5 excercise_1 for string
# date : 2019.3.22
# author by : qiming

# 原始文本
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

# 将全部better变换为worse
txt1 = text.replace('better','worse')
# 大写字母转换成小写，小写转换成大写
txt2 = txt1.swapcase()
# 剔除标点，将所有单词按a…z升序排列，同时转换为列表
list1 = txt2.split( )
i=0
for i in range(0,len(list1)):
    list1[i]=list1[i].strip('*-,.!')
    if list1[i]==' ': 
        list1[i].remove(' ')
    else:
        i=i+1
list2 = sorted(list1)
# 剔除包含‘ea’的英文单词，同时将列表转换为字符串
str1 = 'EA'
list3 = []
for i in list2:
    if i.find(str1) == -1 :
        list3.append(i)
    else :
        continue
print(' '.join(list3))
