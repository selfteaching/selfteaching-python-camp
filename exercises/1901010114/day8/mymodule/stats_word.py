import re
from collections import Counter
# 统计英文

def stats_text_en(text,count):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型')
    word_list = re.findall(r'\b[a-z]+\'?[a-z]+',text.lower())
    return Counter(word_list).most_common(count)

# 统计中文
def stats_text_cn(text,count):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型')
    text_cn = re.sub(r'[\Wa-zA-Z0-9]','',text) 
    return Counter(text_cn).most_common(count)

def stats_text(text,count):
    list_en = stats_text_en(text,count)
    list_cn = stats_text_cn(text,count)

    return list_en + list_cn


    
    
   
        



