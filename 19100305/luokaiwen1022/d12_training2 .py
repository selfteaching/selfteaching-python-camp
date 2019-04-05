import requests
from pyquery import PyQuery
from mymodule import stats_word

#登陆微信:
from wxpy import * # 导入模块
bot = Bot() # 初始化机器人，扫码登陆

# 搜索名称含有 "xx" 的好友
#my_friend = bot.friends().search('xx')[0]
#my_friend.send('hello,send me something')

#打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    if msg.type =='Sharing':
        response = requests.get(msg.url)    # 请求获得内容
        document = PyQuery(response.text)    # 解析提出内容
        content = document('#js_content').text()
        statList = stats_word.stats_text(content,100)
        statString = ''.join(str(i) for i in statList)
      
        msg.reply(statString)

embed() # 让程序保持运行