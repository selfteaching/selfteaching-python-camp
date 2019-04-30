import requests
import pyquery
from pyquery import PyQuery
from mymodule import stats____word
# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()
#定义好友变量
my_friend = bot.friends().search('一', sex=MALE, city="西安")[0] 
# 发送文本给好友
my_friend.send('Hello WeChat!')









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