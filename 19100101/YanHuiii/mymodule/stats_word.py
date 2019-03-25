'''这是一个封装统计英文词频的函数，以及一个封装中文词频的函数

6.1创建一个名为stats_text_en的函数，并用它封装d5_exercise_stats_text.py文件中的代码 '''

dict1 = {}
dict2 = {}

"""创建一个名为stats_text_en的函数，它的功能是为统计英文词频"""
def stats_text_en(text):
    '''参数类型检查（必须为字符串类型）'''
    while not isinstance(text,str):
        raise ValueError("你输入的内容不是字符串.")
    else:
        pass
    import re
    '''只保留英文'''
    text = re.sub("[^A-Za-z]", " ", text.strip())
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


'''6.2创建一个名为stats_text_cn的函数，并用它实现统计汉字词频的功能'''

def histogram(s, old_d):
    d = old_d
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
"""创建一个名为stats_text_cn的函数，它的功能是为统计中文词频"""
def stats_text_cn(text):
    '''参数类型检查（必须为字符串类型）'''
    while not isinstance(text,str):
        raise ValueError("你输入的内容不是字符串.")
    else:
        pass
    import re
    """去掉text中的英文和数字"""
    text = re.sub("[A-Za-z0-9]", "", text)
    '''将字符串text转换为列表list1,只保留单词为list1中的元素'''
    list1 = re.split(r"\W+",text)   

    '''删除list1中为空的列表元素'''
    while '' in list1:   
        list1.remove('')
    
    ''' 把dict3的行拆成单字，拆成字典格式的'''
    dict1 = dict()
    '''给dict3赋值'''
    for i in range(len(list1)):
        dict1 = histogram(list1[i], dict1)

    """将dict3按照value值从大到小排列，并将结果赋给元组tup1"""
    tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)  

    """遍历元组tup1"""
    for tup1 in tup1:   
            dict2[tup1[0]] = dict1[tup1[0]]  
    return dict2


#7.1定义一个函数stats_text，实现功能为分别调用stats_text_en和stats_text_cn,并叔叔词频统计结果

def stats_text(text):
    '''参数类型检查（必须为字符串类型）'''
    while not isinstance(text,str):
        raise ValueError("你输入的内容不是字符串.")
    else:
        pass
    return (stats_text_en(text),stats_text_cn(text))