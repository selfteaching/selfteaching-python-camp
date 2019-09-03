# 导入模块
from wxpy import *

import requests
import getpass
import yagmail
from pyquery import PyQuery
from mymodule import stats_word

# 初始化机器人，扫码登陆
bot = Bot()
myfriend = bot.friends()
@bot.register(myfriend) 

def reply_my_friend(msg):
    if msg.type =="SHARING":
        print(msg.url)

        response = requests.get(msg.url)
        document = PyQuery(response.text) 
        content = document('#js_content').text()
        
        return  content


# 进入 Python 命令行、让程序保持运行
embed()

