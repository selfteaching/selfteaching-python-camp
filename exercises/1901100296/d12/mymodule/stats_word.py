import collections
import jieba
import requests
import yagmail
import json
from pyquery import PyQuery

# 获取网页内容
def getcontent(url):
    # 请求网页返回内容
    response = requests.get(url)
    # 提取微信公众号正⽂
    document = PyQuery(response.text) 
    content = document('#js_content').text()
    return content


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

    return cnt_words

