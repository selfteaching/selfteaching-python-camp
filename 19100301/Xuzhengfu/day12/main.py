import requests
from pyquery import PyQuery
from stats_word import stats_text
from wxpy import *

bot = Bot()        # 初始化机器人，扫码登录
my_friend = bot.friends()    # 获取所有好友

@bot.register(my_friend,SHARING)    # 仅接受my_friend的share类消息
def reply_my_friend(msg):    # 回复my_friend的消息
    response = requests.get(msg.url)    # 获取分享类消息中的网页URL，使用requests请求并获取返回结果
    document = PyQuery(response.text)   # 获取文本
    content = document('#js_content').text()
    stats = stats_text(content,20)  # 统计词频
    return stats    # 回复统计结果
embed()     # 让程序保持运行