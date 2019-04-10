import re      #这是日常Python编程中不需要的高级函数
text_cn = ''' The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!好好学习，天天向上 '''

def stats_text_cn(text):  #stats 是统计。cn是Chinese。
    # remove chinese symbol and "\n" and " " and, don't forget english and number charactor... 
    i = re.compile("[，；。—~ ？!‘’“”,.* -_ /?;'\nA-Za-z0-9]")
    text_rm_symbol = i.sub("", text)  #？这里的式子不知都什么意思，""这个不知道有什么意义
 
    # split
    text_to_list = []              #定义一个列表
    for x in text_rm_symbol:        #字符串弄成列表的形式
        text_to_list.append(x) 
    while "" in text_to_list:       #去掉""这个东西
        text_to_list.remove("")      #最后剩下只有汉字的列表
    # create dictionary              #创作一个字典
    sort_list = [(x, text_to_list.count(x)) for x in set(text_to_list)]#列表是可变类型，可以用sort对列表进行排序
                                                                       #？不知道set有什么作用
    sort_dict = dict(sort_list)                                        #创造一个字典
    # output a dictionary sort by frequency 
    return (sorted(sort_dict.items(), key=lambda x: x[1], reverse=True)) #lambda是什么意思
     #sorted(iterable, *, key=None, reverse=False)从iterable中的项返回一个新的排序列表。
     #reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
print(stats_text_cn(text_cn))      #字符串的形式

print(dict(stats_text_cn(text_cn)))#字典的形式