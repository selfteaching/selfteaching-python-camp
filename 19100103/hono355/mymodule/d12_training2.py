from wxpy import *
from collections import Counter
import jieba
import pyquery
import requests


bot=Bot()    #初始化机器人，扫码登陆微信网页版
my_friend = bot.friends()  #回复对象为所有好友

#回复 my_friend 发送的消息
@bot.register(my_friend, SHARING)    #接收分享（SHARING）类型消息
def reply_my_friend(msg):
    r = requests.get(msg.url)    #msg.url为分享类型消息的网页链接
    r.text
    from pyquery import PyQuery
    document = PyQuery(r.text)
    content = document('#js_content').text()
    import stats_word1
    result = stats_word1.stats_text_cn(content, 100)
    result_str =  ' '.join([ str(i) for i in result ])
    return result_str    #将结果返回给好友

embed()    #堵塞线程，让程序保持运行，保持监听状态