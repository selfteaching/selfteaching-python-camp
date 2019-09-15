import requests
import pyquery
from wxpy import *
import stats_word

bot = Bot()                  #初始化机器人，扫码登陆
@bot.register(Friend,SHARING)               #监听朋友发的sharing信息
def reply(msg):                                         
    print(msg)
    
    response= requests.get(msg.url)         #提取sharing正文
    document = PyQuery(response.text) 
    content = document('#js_content').text()

    from stats_word_d12 import stats_text   #调用模板,统计
    result=str(stats_text(content))
    return
embed()






