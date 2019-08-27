import json#加载json模块完成对.json文件的读取
import stats_word
import requests
from pyquery import PyQuery
from wxpy import *#加载wxpy模块中所有函数
def get_it(msg) :#定义获取网页内容的函数
    response = requests.get(msg)
    document = PyQuery(response.text)
    return document('#js_content').text()
bot = Bot()#登录账号
friend = bot.friends()#获取所有好友
@bot.register(friend,SHARING)#检测所有好友发来消息中的sharing类型的消息
def statistics(msg):#以捕获的网页连接为参数，获取其中内容的词频统计结果
    content = get_it(msg.url)#获取网页内容
    result = stats_word.stats_text_cn(content,100)#对网页内容进行词频统计
    msg.reply(str(result))
embed()