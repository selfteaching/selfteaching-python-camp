import re
from collections import Counter

def stats_text_en(text,x):
    """统计输入文本中的英文字频，从大到小排序"""
    if type(text)!=str:
        raise ValueError("Could not deal with this data,please check it and try again.")
    list_en=re.findall('[a-zA-Z0-9]+',text) #提取英文单词形成列表
    count=int(x)
    return Counter(list_en).most_common(count)
    
  
################################
def stats_text_cn(text,x):
    """统计输入文本中的中文字频，从大到小排序"""
    if type(text)!=str:
        raise ValueError("Could not deal with this data,please check it and try again.")
    list_cn=re.findall(u'[\u4e00-\u9fa5]',text)
    
    count=int(x)
    return Counter(list_cn).most_common(int(count))
    
def stats_txt(text,x):
    if type(text)!=str:
        raise ValueError("Could not deal with this data,please check it and try again.")
    list_cn=re.findall(u'[\u4e00-\u9fa5]',text)
    list_en=re.findall('[a-zA-Z0-9]+',text)    
    list_txt=list_cn+list_en
    count=int(x)
    return Counter(list_txt).most_common(count)

