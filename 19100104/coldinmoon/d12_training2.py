
#将实战项目1功能定义为函数
def word_frequency_analysis(url):
    #使用requests请求微信公众号链接，获取返回结果
    import requests

    response=requests.get(url)

    #将response.text用pyquery把微信公众号正文提取出来
    from pyquery import PyQuery as pq

    document=pq(response.text)
    content=document('#js_content').text()

    #使用stats_word中stats_text_cn分析统计前100词频结果
    from mymodule.stats_word import stats_text_cn as stc

    result=stc(content,100)
    result=str(result)
    return result

#引入wxpy模块
from wxpy import *

bot=Bot(cache_path=True)    #初始化机器人

@bot.register(Friend,SHARING)   #接收SHARING类信息
def auto_reply_analysis_result(msg):  #注册自动回复词频
        result=word_frequency_analysis(msg.url) #分析通过监听获取的网页链接
        return result   #回复分析结果

embed() #保持监听