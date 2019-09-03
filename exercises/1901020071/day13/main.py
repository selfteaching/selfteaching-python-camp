from mymodule import stats_word
from collections import Counter
from wxpy import *

import jieba
import requests
from pyquery import PyQuery
import yagmail
import getpass


# response=requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")

# document=PyQuery(response.text)
# content = document('#js_content').text()



# #把文件里的汉字进行词频统计，并返回
# countList=stats_word.stats_text_cn(content,100)
# countList=str(countList)
#初始化机器人对象
bot=Bot()
#定位好友惜时
friend=bot.friends().search("惜时")[0]

@bot.register(Friend)
def print_others(msg):
    if msg.chat==friend:
        if msg.type == 'Sharing':
            #爬去url页面
            response=requests.get(msg.url)
            document=PyQuery(response.text)
            #获取url文章内容
            content = document('#page-content').text()
            #统计词频钱20的词语
            countList=stats_word.stats_text_cn(content,20)

            print(countList)
            countList=str(countList)

            msg.chat.send_msg(msg.chat.nick_name+" : "+countList)
        else:
            msg.chat.send_msg(msg.chat.nick_name+" : "+msg.text)
       # msg.forward(friend, prefix='老板发言')
    #print(msg.url)
    #print(msg.chat)
    #msg.forward(friend)
    #print(msg.split(" :")[0])
embed()    

    




