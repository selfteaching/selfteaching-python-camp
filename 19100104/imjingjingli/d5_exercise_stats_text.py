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
text_list = re.split(r'[\s,.!\-*]', text)  #用空格 、 ， . --  *将字符串切片，返回字符串列表text_list；r表示不转义，使用真实字符

text_dict = dict()  #建一个空字典
for i in text_list:  #遍历整个列表执行以下操作
    if i:                         #判断字符串
        if i in text_dict:        #如果在字符串在字典中，那么执行执行以下操作
            text_dict[i] += 1     #将键的关联值加1
        else:                     #否则，执行以下操作
            text_dict[i] = 1      #字符串没有在字典中出现过，添加 键-值 一对，且将对应键的值设为1
#print(text_dict)

text_dict_sorted = sorted(text_dict.items(), key = lambda x:x[1], reverse=True)  #sorted按照对应键值由大到小进行排列，以列表返回可遍历的(键, 值) 元组数组，reverse = True 降序
print(text_dict_sorted)
