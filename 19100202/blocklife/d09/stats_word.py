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
Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，
最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，
越来越多被用于独立的、大型项目的开发。'''

# fuctinon 1：英文单词的词频：
def stats_text_en(text):
    import collections
    if not isinstance(text,str): # Day8 添加参数类型检查
        raise ValueError('输入的不是文本格式，请重新输入：') 
    text = text.replace('.', '').replace('!', '').replace('--', '').replace('*', '').replace(',', '').replace('(', '').replace(')', '').replace(';', '').replace(':', '').replace('\'', '').replace('?', '').replace('_', '').replace('-', '').replace('/', '') .replace('[', '') .replace(']', '') .replace('\\', '') .replace('\"', '').replace('{', '').replace('}', '').replace('\t', '').replace('\n', '').replace('\r\n', '')    # 去除各种标点符号和空格
    list_text = text.split() # 将string转换为list
    count = int(input("请输入要限制输出的元素个数："))
    dic = collections.counter(list_text).most_common(count)
    return dic

# function 2：中文字的词频：
def stats_text_cn(text):  
    dic = {} # local variable 
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：') # Day8 
    
    for i in text:  # 这一串汉字是一个字符串，i代表了每个汉字的unicode编码
        if u'\u4e00' <= i <= u'\u9fff':     # 挑选出中文字 ????????????
            dic[i] = text.count(i)      # 用.count()函数/方法来对每个元素（这里是汉字）进行计数，形成一个字典
    import collections
    count = int(input('请输入要限制输出的元素个数：'))
    dic = collections.Counter(dic).most_common(count)  #按出现次数从大到小排列
    return dic


# 函数3：统计中英文混合词频：
def stats_text(text):
    '''函数说明：本函数的功能是统计输入文本的汉字及英语单词词频，并以降序排列输出。'''
    dic_1 = stats_text_cn(text) # Call function 1 
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：') # Day8 
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff': #repeat the function 2 
            text = text.replace(i,"") 
    text = text.replace('「', '').replace('」', '').replace('，', '').replace('。', '').replace('：', '').replace('？', '').replace('！', '')
    # 以上一句删除所有中文标点
    dic_2 = stats_text_en(text) # Call function 2 
    dic_3 = {}
    dic_3.update(dic_2)
    dic_3.update(dic_1) # 将之前分别得到的两个中英文词频结果字典合并
    dic_3 = sorted(dic_3.items(),key = lambda x:x[1],reverse = True) # 对合并后的字典进行排序，得出混合排序结果

    return(dic_3)


print(stats_text.__doc__)