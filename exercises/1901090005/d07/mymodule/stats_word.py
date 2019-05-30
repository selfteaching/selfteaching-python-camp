def stats_text_en(text):  #定义函数
    import re
    a = re.sub('[^a-zA-Z ]',' ',text) #只保留英文
    b = a.split()  #切割成列表
    c = {}     #定义空字典
    for en in b:
        value = c.get(en,0) #获取单词统计数量
        value += 1 
        c[en] = value 
    d = sorted(c.items(), key=lambda x:x[1], reverse=True) #降序排序
    return d

def stats_text_cn(text):  # 定义函数
    e = {} #定义空字典
    for ch in text:
        if u'\u4e00' <= ch <= u'\u9fff': #中文字符范围，判断中文字符
            value =e.get(ch,0)  #获取汉字统计数量
            value += 1
            e[ch] =value
    f = sorted(e.items(), key=lambda item: item[1], reverse=True)  #降序排序
    return f    


def stats_text(text):  # 定义函数
    dict1 = stats_text_cn(text)
    dict2 = stats_text_en(text)
    dict3 = dict1+dict2 # 合并汉字和英语字数统计数量
    return dict3






