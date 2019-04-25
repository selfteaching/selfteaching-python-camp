from wxpy import *
import requests
from pyquery import PyQuery
import stats_word as sw
import d13_training3 as dt

bot = Bot() #初始化 / 登录

@bot.register([Group,Friend], SHARING, except_self = False)
def word_frequency(meg) :

    response = requests.get(meg.url) #请求连接，并读取内容

    document = PyQuery(response.text)
    content = document('#js_content').text() #将内容提取出来

    list_a = sw.stats_text(content,10) #对内容进行分词，取其前100个频率的词汇
    
    meg.reply_image(dt.map_making(list_a))
    
    return 


embed()