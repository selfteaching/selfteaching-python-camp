import requests
from pyquery import PyQuery
from mymodule import stats_word


# 通过url获取文本
def stats (url) :
    response = requests.get(url)
    # 提取公众号正文
    document = PyQuery (response.text)
    content = document ('#js_content').text() 
    # 统计前100词频
    statList = stats_word.stats_text(content,100)
    statString = ''.join(str(i) for i in statList)

    return statString