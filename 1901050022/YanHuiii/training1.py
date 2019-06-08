'''这是一个通过网络请求获得网页内容，使用分词工具对中文字符串
进行分词，统计词频，返回结果'''
import requests
import pyquery
from pyquery import PyQuery
from mymodule import stats_word
def stats_meg(url):

    '''获取网址'''
    image_url = url

    '''将网址中的内容全部赋值给response'''
    response = requests.get(image_url)

    '''提取网址中的正文内容'''
    document = pyquery.PyQuery(response.text)
    content = document('#js_content').text()
    
    '''返回网址正文中前100位的中文词频结果'''
    return stats_word.stats_text_cn(content,100)
