from wxpy import *
import requests
from pyquery import PyQuery
from mymodule import stats_word
#初始化机器人，扫码登陆
bot = Bot()
#指定特选好友燃烧的手指并发送消息
my_friend = bot.friends().search("燃烧的手指")[0]
my_friend.send('你今天好漂亮,给我分享一篇文章吧！')

@bot.register(my_friend)
def print_others(msg):
    if msg.type == 'Sharing':#如果是sharing类型
        r = requests.get(msg.url)#使用requery获取微信公众号文章
        document = PyQuery(r.text)#提取公众号正文
        content = document('#js_content').text()#提取公众号正文
        result = stats_word.stats_text(content,100)#使用模块统计结果并赋值给result
        my_friend.send(result)#发送result的内容给好友

embed()     


    

