import re
def stats_text_en(text):
    """统计英文文本的词频
    
    返回list形式的数据"""
    word_dict = {}
    for word in text.split():
        match_obj = re.search('([a-zA-Z]+)', word)
        if match_obj is not None:
            w = match_obj.group(1).lower()
            if w in word_dict:
                word_dict[w] += 1
            else:
                word_dict[w] = 1

    # 参考：https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
    return sorted(word_dict.items(), key=lambda item: item[1], reverse=True)

def stats_text_cn(text):
    """统计中午文本的字频
    
    返回list形式的数据"""
    word_dict = {}
    # for word in text.split(''):
    for word in text:
        if '\u4e00' <= word <= '\u9fff':
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return sorted(word_dict.items(), key=lambda item: item[1], reverse=True)

def stats_text(text):
    """统计中文、英文文本的词频
    
    返回list形式的数据"""
    word_list_en = stats_text_en(text)
    word_list_cn = stats_text_cn(text)
    return sorted(word_list_en + word_list_cn, key=lambda item:item[1], reverse=True)
