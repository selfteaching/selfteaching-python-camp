import re
from collections import Counter
count = int()
#英文字符排序
def stats_text_en(text, count):
    #如果不是字符串，抛异常，异常会终止代码执行
    if not isinstance(text, str):
        raise TypeError ('输入有误, 请输入字符串')
    #如果没有抛出异常，代表是字符串
    en = re.sub(r'[^A-Za-z]',' ', text) #仅挑出英文字符，略过中文
    text_1 = en.lower().split() #组成列表    
    return Counter(text_1).most_common(count)

#中文字符排序
def stats_text_cn(text, count):
    if not isinstance(text, str):
        raise TypeError ('输入有误, 请输入字符串')
    cn = re.findall(r'[\u4E00-\u9FFF]', text) #\u4E00-\u9FFF代表取出中文字符
    return Counter(cn).most_common(count)

