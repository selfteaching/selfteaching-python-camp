import requests
import stats____word
import getpass
from pyquery import PyQuery
# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()

 #定义好友变量
my_friend = bot.friends().search('一', sex=MALE, city="西安")[0] 

 # 发送文本给好友
my_friend.send('Hello WeChat!')

 # 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)

 # 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(my_friend)
def reply_my_friend(msg):
    return '收到消息: {} ({})'.format(msg, msg.type)

 # 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')

 #接收share类信息
@bot.register(my_friend,SHARING) #接受分享类消息
def auto_reply(msg):
    response = requests.get(msg.url) #msg.url为分享的网址
    document = PyQuery(response.text)
    content = document('#js_content').text()
    #处理文本
    result = stats____word.stats_text_cn(content,count=100)
    return result #将结果返回给好友

embed() #保持监听状态 
