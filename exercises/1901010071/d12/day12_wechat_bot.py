import requests
import pyquery
from pyquery import PyQuery
import stats_word

from wxpy import * #  导入微信机器人模块
bot = Bot() #初始化机器人，扫码登录

# 搜索名称含有 "xx" 的好友,sex=MALE(或者FEMALE)
my_friend = bot.friends().search('xx',sex=FEMALE,city='San Diego City')[0]
# 发送文本给好友
my_friend.send('请分享一篇文章给我')

@bot.register()
def print_others(msg):
    if msg.type == 'Sharing': #sharing 分享的公众号文章
        r = requests.get(msg.url) #解析获取公众号文章的url
        document = PyQuery(r.text)
        content = document('#js_content').text()
        r_list = stats_word.stats_text(content,100)
        r_str = str(r_list)
        msg.reply(r_str) # 自动回复返回的参数

embed() # 让程序保持运行
