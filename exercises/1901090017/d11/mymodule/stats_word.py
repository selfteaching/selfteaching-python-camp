import jieba
from collections import Counter

 

def stats_text_cn(text,count):
    if not isinstance(text, str):
        raise ValueError('参数必须是 str 类型')
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    text2 = "".join(cn_characters)
    cn_text = jieba.cut(text2, cut_all=False)
    cn_word_counter = Counter()
    for cn_word in cn_text:
        if len(cn_word) >= 2:
            cn_word_counter[cn_word] += 1
        else:
            pass

    return cn_word_counter.most_common(count)
 
 