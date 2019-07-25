import re

def stats_text_en(text):
    '''统计字符串里每个英文单词的词频，返回按照词频降序排列的数组'''
    
    #字符串类型监测
    if type(text)!= str:
        raise ValueError(f'传入的是{type(text)}类型,请传入字符串')

    #提取字符串里的英文单词
    word_list = re.findall('[A-Za-z]+', text)
    #统计词频
    Word_dict = {word:word_list.count(word) for word in word_list}
    #排序
    result = sorted(Word_dict.items(),key = lambda items:items[1],reverse = True)
    #print(result)
    return result

def stats_text_cn(text):
    '''统计字符串里每个汉字的词频，返回按照词频降序排列的数组'''
    
    #字符串类型监测
    if type(text)!= str:
        raise ValueError(f'传入的是{type(text)}类型,请传入字符串')

    #提取字符串里的英文单词
    word_list = re.findall('[\u4e00-\u9fa5]', text)
    #统计词频
    Word_dict = {word:word_list.count(word) for word in word_list}
    #排序
    result = sorted(Word_dict.items(),key = lambda items:items[1],reverse = True)
    #print(result)
    return result

def stats_text(text):
    '''分别调⽤stats_text_en , stats_text_cn ，输出合并词频统计结果'''
    
    #字符串类型监测
    if type(text)!= str:
        raise ValueError(f'传入的是{type(text)}类型,请传入字符串')

    result = stats_text_en(text) + stats_text_cn(text)
    print(result)
    return result

a = [1]
stats_text(a)
