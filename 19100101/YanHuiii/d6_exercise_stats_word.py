'''这是一个封装统计英文词频的函数，以及一个封装中文词频的函数

6.1创建一个名为stats_text_en的函数，并用它封装d5_exercise_stats_text.py文件中的代码 '''

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
dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}

"""创建一个名为stats_text_en的函数，它的功能是为统计英文词频"""
def stats_text_en(text):
    import re
    '''将字符串text转换为列表list1,只保留单词为list1中的元素'''
    list1 = re.split(r"\W+",text)   
    '''删除list1中为空的列表元素'''
    while '' in list1:   
        list1.remove('')
    """i属于list1中的元素，开始循环"""
    for i in list1:   
        """将列表中的单词及单词的出现次数，分别赋值给dict1的键和值"""
        dict1.setdefault(i,list1.count(i))  
    """将dict1按照value值从大到小排列，并将结果赋给元组tup1"""
    tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)   
    """遍历元组tup1"""
    for tup1 in tup1:   
            dict2[tup1[0]] = dict1[tup1[0]]  
    return dict2

#打印统计英文词频的结果
print("统计英文词频的结果为:")
print(stats_text_en(text))
str = ''


'''6.2创建一个名为stats_text_cn的函数，并用它实现统计汉字词频的功能'''

"""创建一个名为stats_text_cn的函数，它的功能是为统计中文词频"""
def stats_text_cn(text):
    import re

    '''将字符串text转换为列表list1,只保留单词为list1中的元素'''
    list1 = re.split(r"\W+",text)   

    '''删除list1中为空的列表元素'''
    while '' in list1:   
        list1.remove('')
    
    """i属于list1中的元素，开始循环"""
    for i in list1:   
        """判断是否为中文字"""
        if i >= u'/u4e00' and i <= u'/u9fa5':
            """将列表中的单词及单词的出现次数，分别赋值给dict1的键和值"""
            dict3.setdefault(i,list1.count(i))  

    """将dict1按照value值从大到小排列，并将结果赋给元组tup1"""
    tup1 = sorted(dict3.items(),key = lambda items:items[1],reverse = True)  

    """遍历元组tup1"""
    for tup1 in tup1:   
            dict4[tup1[0]] = dict3[tup1[0]]  
    return dict4

#打印统计中文词频的结果
print("统计中文词频的结果为:")
print(stats_text_cn(text))