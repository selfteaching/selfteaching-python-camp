import requests
import stats_word as sw
from pyquery import PyQuery as py
from wxpy import *

#初始化 扫码登录
bot = Bot()
my_friend = bot.friends()

@bot.register(my_friend)
def step1(msg):
        if msg.type == 'Sharing': #如果msg的类型是Sharing类型
                r = requests.get(msg.url) #获取msg的网页链接
                #print(r)
                #用requests请求获取公众号文章的链接
                document = py(r.text) 
                #print(document)
                content = document('#js_content').text()
                #print(content)
                #用stats_text_cn将获取的链接结果进行分析和词频统计
                result = sw.stats_text_cn(content,100)
                #print(result)
                return result

embed()


