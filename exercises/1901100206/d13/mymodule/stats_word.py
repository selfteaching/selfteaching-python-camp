# encoding=utf-8
import re, jieba
from collections import Counter
count = int()
def stats_text_cn(text, count):
    if not isinstance(text, str):
        raise TypeError ('输入有误, 请输入字符串')
    cn = re.sub('[^\u4e00-\u9fa5]','',text) #将所有非中文字符替换为空
    cn_list = jieba.lcut(cn)  # 默认是精确模式，lcut返回list
    cn_list1 = []
    for i in cn_list: #只统计长度大于等于2的词
        if len(i) >= 2:
            cn_list1.append(i)
    return Counter(cn_list1).most_common(count)
    

