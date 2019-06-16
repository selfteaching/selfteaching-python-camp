
import re
import collections
from collections import Counter
import jieba
import requests

def stats_text_cn(t_cn,count): 
    if type(t_cn) == str:
        text_cn = re.findall(u'[\u4e00-\u9fff]+', t_cn)
        seg_list = jieba.cut(' '.join(text_cn))
        cn_list = []
        for i in seg_list:
            if len(i) >= 2:
                cn_list.append(i)
        return Counter(cn_list).most_common(count)
    else:
        raise ValueError("输入不为字符串")

def request_date(url):
    from pyquery import PyQuery
    response = requests.get('url')
    document = PyQuery(response.text)
    content = document('#js_coment').text()
    return content
    
