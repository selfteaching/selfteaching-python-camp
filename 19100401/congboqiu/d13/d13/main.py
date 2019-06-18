import re
import jieba
import getpass
import requests
import wxpy
from pyquery import PyQuery
from mymodule import stats_word

#导入模块wxpy，建微信机器人
from wxpy import *
bot=Bot(cache_path=True)
my_friend=bot.friends().search('翕羊羊')[0]
my_friend.send('你好，请分享篇文章给我')#发消息给朋友


@bot.register(my_friend,msg_types='Sharing')
def auto_reply(msg):
    print(msg)
    print(msg.url)
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    text=content
    
    #引入变量words和count，为图像化函数做好参数引入
    dict_text=dict(stats_word.stats_text_cn(text,10)) #把结果转化字典
    key_words=list(dict_text.keys())#把字典的key和对应值转换为列表
    count_values=list(dict_text.values()) #把字典的value和对应值转换为列表
   
    #用matplotlib把words和count图像化
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcdefaults()
    fig,ax = plt.subplots()
    plt.rcParams['font.sans-serif']=['SimHei'] 
    ax.barh(key_words,count_values, align = "center", color = "blue")
    ax.set_yticks(key_words)
    ax.set_yticklabels(key_words)
    ax.invert_yaxis()
    ax.set_xlabel(count_values)
    ax.set_title('你刚才所发文章的词频前10统计')
    
    plt.savefig('result.png')
    msg.reply_image('result.png')
    
embed()

