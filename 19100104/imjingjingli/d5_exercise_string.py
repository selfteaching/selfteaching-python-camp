import re
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
new_text_list2 = []  #创建空列表
text_list = re.split(r'[\s,.!\-*]', text)   #用空格 、 ， . --  *将字符串切片，返回字符串列表text_list；r表示不转义，使用真实字符


for i in text_list:                      #遍历整个列表text_list，对每个元素执行如下操作
    if i and 'ea' not in i:              #如果字符串中不含"ea"
        new_text_list2.append(i)         #就将这个值加入new_text_list2的末尾


new_text_list3 = []                      #创建空列表new_text_list3
for i in new_text_list2:                 #遍历整个new_text_list2，对每个元素执行如下操作
    if i == 'better':                    #如果字符串是better
        new_text_list3.append('worse')   #将字符串worse加入到列表new_text_list3的末尾
    else:                                #否则就将字符串加入到列表new_text_list3的末尾
        new_text_list3.append(i)


new_text_list4 = []                      #创建空列表new_text_list4
for i in new_text_list3:                 #遍历整个列表new_text_list3执行如下操作
    new_str = i.swapcase()               #用swapcase()于对字符串的大小写字母进行转换
    new_text_list4.append(new_str)       #将字符串逐个加入到列表的末尾


new_text_list5 = sorted(new_text_list4, reverse=False)  #用sorted函数对字符串按照首字母升序排列
print(new_text_list5)