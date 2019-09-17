import collections
import jieba
import json

# 封装统计汉字词频的函数
def stats_text_cn(text,count):
    if type(text)!=str:
        raise ValueError('输入类型 %s,参数必须是 str 类型'%type(text))
    # 使用jieba分词
    seg_words = jieba.cut(text)
    # 长度大于等于2的词
    words = []
    for word in seg_words:
        if len(word) >= 2:
            words.append(word)
    # 使用标准库的Counter统计词和词频数，返回前count位的数据
    cnt_words = collections.Counter(words).most_common(count)
    # res_words = str(cnt_words)
    res_words=''
    for r in cnt_words:
        a,b = r
        w = a + ':' +str(b)
        # print(w)
        res_words = res_words + '\n' + w
        
    return res_words
