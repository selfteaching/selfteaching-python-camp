

import requests
from pyquery import PyQuery
from mymodule import stats_word


# 定义stats函数，通过url获取文本并分析
def stats (url,num) :
    response = requests.get(url)
    # 提取微信公众号正文
    document = PyQuery (response.text)
    content = document ('#js_content').text() 
    # 统计前100词频
    statList = stats_word.stats_text(content,num)
#    statString = ''.join(str(i) for i in statList)
    statDict = dict(statList)
    return statDict

