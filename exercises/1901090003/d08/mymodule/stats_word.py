import re
# 统计英文
def stats_text_en(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型')
    word_list = re.findall(r'\b[a-z]+\'?[a-z]+',text.lower()) 
    count_dict = {}
    for word in word_list:
        count_dict[word] = word_list.count(word)
    list_en = sorted(count_dict.items(), key = lambda x: x[1], reverse=True) 
    return list_en
# 统计中文
def stats_text_cn(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型')
    text_cn = re.sub(r'[\Wa-zA-Z0-9]','',text) 
    count_dict = {}
    for character in text_cn:
        count_dict[character] = text_cn.count(character)
    list_cn = sorted(count_dict.items(), key = lambda x: x[1], reverse=True) 
    return list_cn

def stats_text(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型')
    list_en = stats_text_en(text)
    list_cn = stats_text_cn(text)
    list_all = sorted((list_en + list_cn), key = lambda x: x[1], reverse=True) 
    return list_all