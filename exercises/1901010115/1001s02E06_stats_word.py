text1 = '''
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

def stats_text_en(t): #定义函数，参数为t
    t = t.lower() #文本转小写
    t_list = t.split() #文本转列表
    t_dict = {} #新建一个空字典
    for i in t_list: #指定i遍历上述列表
        ii = i.strip(' ,.*!-') #清洗i中元素
        if ii not in t_dict: #如果单词不在新建字典中
            t_dict[ii] = 1 #则字典添加单词
        else: #如果单词已在新建字典中
            t_dict[ii] = t_dict[ii] + 1 #则该单词对应的计数增加1
    t_dict_sorted = sorted(t_dict.items(),key = lambda x:x[1],reverse = True) #items()函数用于把字典转为元组；key=lambda x:x[1]用于设定键按值大小排列；reverse=True用于设定键按降序排列
    return t_dict_sorted #返回函数结果
print('text1:')
print(stats_text_en(text1))
print('\n')



text2 = '''
/“/请/！/”/“/请/！/”/两名/剑士/各自/倒转/剑尖/，/右手/握/剑柄/，
/左手/搭于/右手/手背/，/躬身行礼/。/两/人/身子/尚未/站/直/，
/突然/间/白光闪/动/，/跟着/铮的/一/声响/，
/双剑相/交/，/两/人/各/退一步/。
/旁/观众/人/都/是/“/咦/”/的/一声/轻呼/。/青衣/剑士/连/劈/三/剑/
'''

text3 = '''
二 结构化思维，几乎是最值得刻意训练的能力！
然而在现实中，很多人往往忽略结构化思维的培养，因为他们认为，这是天生的。他们要么觉得自己足够聪明所以不需要培养，要么觉得我天生不聪明，学不来，干脆放弃。
我曾经在文章中提到过能力的重要性。有人问，能力有那么多，到底培养哪一个才好呢？如果我用一个两维矩阵来分析的话，可以看到，结构化思维能力，是既能够被培养同时价值度又高的能力。
'''

def stats_text_cn(t): #定义函数，参数为t
    t_list = [] #新建一个空列表
    t_dict = {} #新建一个空字典
    exclude_str = '\n ，。！？/”“' #新建一个字符串,备用（将要消除的中文符号）
    for char in t: #遍历文本中的字节
        t_list.append(char) #把拆解的所有字节（包括单个汉字和符号）放入新建的列表中
    for char in t_list: #遍历列表中的元素
        if char not in exclude_str: #如果该字节为汉字，不是符号
            if char.strip() not in t_dict: #又如果（strip(）用于消除空格）汉字不在新建的字典中
                t_dict[char] = 1 #则字典添加汉字
            else: #如果汉字已在字典中
                t_dict[char] = t_dict[char] + 1 #则对字典中该单词对应的计数增加1
    t_dict_sorted = sorted(t_dict.items(),key = lambda x:x[1],reverse = True)#items()函数用于把字典转为元组；key=lambda x:x[1]用于设定键按值大小排列；reverse=True用于设定键按降序排列
    return t_dict_sorted #返回函数结果
print('text2:')
print(stats_text_cn(text2))
print('\n')
print('text3:')
print(stats_text_cn(text3))