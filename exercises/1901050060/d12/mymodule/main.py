import stats_word
import requests
from pyquery import PyQuery
from wxpy import *


bot = Bot()
@bot.register()
def print_others(msg):
    '''1、先判断消息是Sharing类型，获取URL并对文本进行统计，输出前100的词频'''
    if msg.type == 'Sharing':#如果是sharing类型
        response = requests.get(msg.url)#msg.url为分享的网址
        document = PyQuery(response.text)
        content = document('#js_content').text()
        #结巴处理
        result = stats_word.stast_text_cn(content,count=100)
        msg.reply(result)  #发送result的内容给好友

embed()

