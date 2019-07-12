

from wxpy import *
'''
# encoding=utf-8
import jieba
import yagmail
import requests
from pyquery import PyQuery
from collections import Counter

from mymodule import stats_word
import getpass
import logging
'''
# 提取公众号文章里的正文内容并统计词频前100的词汇

# def get_article(path):
#     # 链接获取的内容
#     response = requests.get(path, auth=('user', 'pass'))
#     # 提取正文
#     document = PyQuery(response.text) 
#     # 返回正文字符串
#     return  document('#js_content').text()

# 初始化机器人，扫码登陆
bot = Bot()

# 搜索名称含有 "xx" 的男性深圳好友
my_friend = bot.friends().search('党聪', sex=MALE, city="深圳")[0]

# 发送文本给好友
my_friend.send('Hello WeChat!')
# 发送图片
my_friend.send_image('my_picture.jpg')

@bot.register()
def print_others(msg):
    if msg.type == "Sharing":
    #    print(get_article(msg.url))
        pass
    print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(my_friend)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

embed()    
