import collections
import re
import jieba
count = int()

def stats_text_en(text,count):  #定义函数
    if not isinstance(text,str):
        raise ValueError('输出有误，请重新输入：') 
    a = re.sub('[^a-zA-Z ]',' ',text) #只保留英文
    b = a.split()  #切割成列表
    return collections.Counter(b).most_common(count)

def stats_text_cn(text,count):  # 定义函数
    if not isinstance(text,str):
        raise ValueError('输入有误，请重新输入：') 
    text = jieba.cut(text,cut_all=False)
    e = {} #定义空字典
    for ch in text:
        if len(ch) >= 2 and u'\u4e00' <= ch <= u'\u9fff': #中文字符范围，判断中文字符
            value =e.get(ch,0)  #获取汉字统计数量
            value += 1
            e[ch] =value
    return collections.Counter(e).most_common(count)

def stats_text(text,count):
    if not isinstance(text,str):
        raise ValueError('输入有误，请重新输入：') 
    #dict1 = stats_text_cn(text)
    #dict2 = stats_text_en(text)
    #dict3 = dict1+dict2
    #return dict3
    return collections.Counter(stats_text_en(text,count)+stats_text_cn(text,count)).most_common(count)

