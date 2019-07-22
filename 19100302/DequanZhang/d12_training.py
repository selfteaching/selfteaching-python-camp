import requests
from pyquery import PyQuery
import sys
sys.path.append("/Users/zhangdequan/Documents/GitHub/selfteaching-python-camp/19100302/DequanZhang/mymodule")
from stats_word import stats_text_cn

from wxpy import *

bot = Bot()
myfriend = bot.friends()

@bot.register(myfriend, msg_types=SHARING)  #消息为SHARING类型时，获取消息的网页链接msg.url，自动返回词频统计结果
def reply_my_friend(msg):
    response = requests.get(msg.url)    
    document = PyQuery(response.text)
    content = document('#js_content').text()
    statlist = stats_text_cn(content,100)
    return statlist

embed()   #进入Python命令行，让程序保持运行

#或者仅仅堵塞线程
#bot.join()

