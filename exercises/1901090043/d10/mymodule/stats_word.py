import re
from os.path import *
from collections import Counter
import jieba
#字符串文本按照单词排序
def stats_text_en(text,count):
    pattern = re.compile( "[A-Z]*[a-z]+")
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 9') 
    
    word_list = re.findall(pattern,text)
    
    return dict(Counter(word_list).most_common(count))

#参数：字符串文本，输出按汉子的统计排名
def stats_text_cn(text,count):
    pattern1 = re.compile( "[\u4E00-\u9FA5]+")
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 27') 
#找到所有中文汉字
    new_list = re.findall(pattern1,text)
    new_string = ''
    for items in new_list:
        new_string = new_string + items
    
#用结巴函数进行分词，得到列表
    new_string = list(jieba.cut(new_string))
    #删除为一个字的词
    for items in new_string:
        if len(items) == 1:
            new_string.remove(items)

    new_dic = {}
    new_dic = dict(Counter(new_string).most_common(count))

    return new_dic

#调用stats_text_en()，stats_text_cn()两个函数并且合并排序输出
def stats_text(text,count):   
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 46') 

    dic = stats_text_en(text)
    dic1 = stats_text_cn(text)
    #合并dic，dic1
    merge_dic = dict(dic,**dic1)
    
#对新字典排序统计
    dic_result = Counter(merge_dic).most_common(count)

    return dic_result
    
    

