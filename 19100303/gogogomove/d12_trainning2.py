import requests
from pyquery import PyQuery
import sys
sys.path.append("/Users/SeanChen/Documents/GitHub/selfteaching-python-camp/19100303/gogogomove/mymodule")
from stats_word import stats_text_cn

from wxpy import * #导入wxpy模块
bot = Bot() #初始化之
myfriend = bot.friends()

@bot.register(myfriend, msg_types=SHARING)  #消息为SHARING类型，获取消息的网页链接msg.url
def reply_to_my_friend(msg):
    response = requests.get(msg.url)    
    document = PyQuery(response.text)
    content = document('#js_content').text()
    statlist = stats_text_cn(content,100)
    return statlist

embed()   #进入Python命令行，让程序保持运行

