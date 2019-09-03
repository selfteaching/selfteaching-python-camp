# 导入模块
from wxpy import *
import requests
from mymodule import stats_word_d12
from pyquery import PyQuery
'''
当好友向你发送消息后，如果为 分享 (SHARING) 类型的消息，则获取消息的网页链接（msg.url）
将获取的链接使用代码进行处理
将处理结果返回给发送消息过来的好友
'''

# 初始化机器人，扫码登陆
bot = Bot()

@bot.register(msg_types = SHARING)  
def reply_my_friend(msg):  

#使用request请求信息中的url
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()

#使用stats_word 中的 stats_text 对提取结果进行分析和词频统计处理（返回前20个词的统计结果），将结果转换成 str 类型
    result = str(stats_word_d12.stats_text_cn(content,20))
    msg.reply(result)  #将处理结果返回给发送消息过来的好友
embed()

