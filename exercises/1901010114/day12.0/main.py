

from mymodule.stats_word import stats_text as a
from mymodule import stats_word as a
import requests
from pyquery import PyQuery
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties 
# 初始化机器人，扫码登陆
#<<<<<<< master
bot=Bot()
#定位好友豆彭

my_friend = bot.friends().search('豆彭')  #定位朋友
#预先注册，利用Bot.register()完成
#Bot.register(chats=None,msg_types=None,except_self=True,run_async=True,enable=True)
@bot.register(chats = my_friend,msg_types = 'Sharing',except_self = True)
def auto_reply(msg):
    import requests
   
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    
    msg1 = a(content,100)
    return msg1
embed()
#=======
bot = Bot()
# 搜索好友,但没有指定好友的名称
# 搜索名称含有 "游否" 的男性深圳好友
my_friend = bot.friends().search('豆彭')[0]   #找寻名称为豆彭的好友，后面的[0]是什么意思？


#微信机器人启动了，现在要完成对好友的自动监听，一旦发送类型为sharing 的消息，获取这个消息的url并使用项目一中的代码进行分析并
#返回
@bot.register(chats = my_friend, msg_types = 'SHARING') #注册
def auto_reply(msg):     #定义一个自动回复的函数，在这一部分有一个大致的思路，但是到了具体细节写不出来是参考了同学的作业写出来的，但是我想知道到哪找
#答案也是一个很好的方法
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    result = str(stats_word.stats_text_cn(contents,20))
    msg.reply(result)

embed()
   








 
 



#>>>>>>> master
