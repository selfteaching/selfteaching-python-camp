import re
import jieba
import getpass
import requests
from pyquery import PyQuery
from mymodule import stats_word

#导入模块wxpy，建微信机器人
import sys
sys.path.append('c:\\users\\win10\\appdata\\local\\programs\\python\\python37\\lib\\site-packages')
from wxpy import *
bot=Bot(cache_path=True)
my_friend=bot.friends().search('翕羊羊')[0]
my_friend.send('你好，请分享篇文章给我')#发消息给朋友

@bot.register(my_friend,msg_types='Sharing')
def auto_reply(msg):
    print(msg)
    print(msg.url)
    response = requests.get("msg.url")
    document = PyQuery(response.text)
    content = document('#js_content').text()
    print(content)
    text=content
    str_text=str(stats_word.stats_text_cn(text,100))
    my_friend.send(str_text)
    return auto_reply()
embed()

