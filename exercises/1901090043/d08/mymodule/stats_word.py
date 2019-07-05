import re
from os.path import *

#字符串文本按照单词排序
def stats_text_en(text):
    pattern = re.compile( "[A-Z]*[a-z]+")
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 9') 
        
    word_list = re.findall(pattern,text)
    dic = {}
    for item in word_list:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
    dic = sorted(dic.items(),key = lambda x:x[1],reverse = True)

    return dic

#参数：字符串文本，输出按汉子的统计排名
def stats_text_cn(text):
    pattern1 = re.compile( "[\u4E00-\u9FA5]")
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 27') 

    new_list = re.findall(pattern1,text)
    dic1 = {}
    for item in new_list:
        item = item.strip()
        if item not in dic1:
            dic1[item] = 1
        else:
            dic1[item] += 1        
    #降序排列
    dic1 = sorted(dic1.items(),key = lambda x:x[1] ,reverse = True)

    return dic1

#调用stats_text_en()，stats_text_cn()两个函数并且合并排序输出
def stats_text(text):   
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 46') 
    dic = dict(stats_text_en(text))
    dic1 = dict(stats_text_cn(text))

    #合并dic，dic1
    merge_dic = dict(dic,**dic1)
    
#对新字典排序统计
    merge_dic = sorted(merge_dic.items(),key = lambda x:x[1],reverse = True)

    return merge_dic
    
    
    

