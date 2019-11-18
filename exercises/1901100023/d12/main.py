'''
import os
from mymodule import stats_word
from collections import Counter
import json

path = '/Users/hannaspc/Documents/Python/DAY10/d10/tang300.json'
with open (path, 'r', encoding='UTF-8') as f:          # 不加'r', encoding='UTF-8'会报UnicodeDecodeError
    text = f.read()

# 捕获异常
try:
    stats_word.stats_text(text1,20) 
except ValueError:              
    print('Error:文本非字符串')
'''


# day12
from wxpy import *
import requests
import getpass
from pyquery import PyQuery
from mymodule import stats_word

bot = Bot() #登录微信的命令
my_friends = bot.friends().search('韩翊婷')  #搜索名称含有“大头鬼啊-”的好友。bot.friends()→发送给所有好友
#给好友发送信息
#my_friends.send('你好')

#监听好友消息
#通过装饰器，注册一个接收制定好友分享消息的函数
@bot.register(my_friends, SHARING)
def friend_sharing(msg):
    # 使用requests获得网络链接的文本
    address = msg.url
    r = requests.get(address)
    document = PyQuery(r.text)
    content = document('#js_content').text()
    # 将获得的文章进行分词处理
    a = stats_word.stats_text_cn(content, 100)
    b = str(a)
    # 给好友发消息
    my_friends.send(b)
# 让程序保持运行
embed()  # 进入Python命令行

