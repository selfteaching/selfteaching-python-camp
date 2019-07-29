import re
from os.path import *
from collections import Counter
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
    pattern1 = re.compile( "[\u4E00-\u9FA5]")
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 27') 

    new_list = re.findall(pattern1,text)
    
    return dict(Counter(new_list).most_common(count))

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
    
    

