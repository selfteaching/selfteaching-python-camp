from mymodule import stats_word
from pyquery import PyQuery
import requests
from wxpy import *  # 导入模块

bot = Bot() # 初始化机器人，扫码登陆
my_friend = bot.friends().search('阿雙')[0] # 搜索名称含有 "阿雙" 的好友
# 发送文本给好友
my_friend.send('你好! 请分享一篇公众号文章给我，我来给你统计下文章中用到最多的前100个词语。')

@bot.register(my_friend)
def my_friend_SHARING(msg):
    msg = requests.get(msg.url)
    document = PyQuery(msg.text)        
    content = document('#js_content').text()   
    str1 = str(dict(stats_word.stats_text_cn(content,100)))
    my_friend.send(str1)
    
embed() # 进入 Python 命令行、让程序保持运行
