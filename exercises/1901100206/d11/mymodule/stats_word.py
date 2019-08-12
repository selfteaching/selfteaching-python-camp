# encoding=utf-8
import re, jieba, yagmail, requests, pyquery
from collections import Counter
from pyquery import PyQuery
count = int()
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()
def stats_text_cn(text, count):
    if not isinstance(text, str):
        raise TypeError ('输入有误, 请输入字符串')
    cn = re.sub('[^\u4e00-\u9fa5]','',text) #将所有非中文字符剔除
    cn_list = jieba.lcut(cn)  # 默认是精确模式，lcut返回list
    cn_list1 = []
    for i in cn_list: #只统计长度大于等于2的词
        if len(i) >= 2:
            cn_list1.append(i)
            cn_list2 = Counter(cn_list1).most_common(count)
            cn_str = str(cn_list2)
    return cn_str

print(stats_text_cn(content, 100))
