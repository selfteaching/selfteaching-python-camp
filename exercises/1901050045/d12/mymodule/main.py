from wxpy import *
from pyquery import PyQuery
import requests
from stats_word import stats_text
bot=Bot(True)               #启动web微信，设置为True值可以在短时间内不用重复扫码登录
bot.enable_puid()           #不知道干什么用的，但是加入这条命令，就可以在Python里监控微信里收到的信息

friends=bot.friends()

# 打印/监控来自其他好友、群聊和公众号的消息
@bot.register()#参数为空时，默认为所有人
def print_others(msg):
    print(msg)

@bot.register(friends,SHARING)  #SHARING是message类型
def print_link(msg):           
    print('网页链接地址:',msg.url)
    response=requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    #print(content) 查看输出结果
    a= stats_text
    a="".join(str(a(content,100)))
    return a
embed()