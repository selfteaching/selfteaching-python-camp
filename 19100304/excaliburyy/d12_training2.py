# 19100304 day12 银零
# 1.监听好友信息，如果信息为 分享(SHARING)类型的消息，则获取消息的网页链接(msg.url)
# 2.将获取的链接使用 实战项目1 的方式进行处理并将处理结果返回给发送消息过来的好友
# 3.启动微信机器，扫码登录
# 4.使用另一个微信进行测试，观察是否会接收到正确的结果



import requests
import pyquery
from pyquery import PyQuery
from mymodule import stats_word
from wxpy import *

bot = Bot()
my_friend = bot.friends().search('银零',sex = MALE, city = '上海')[0]

@bot.register(my_friend)
def reply_my_friend(msg):
    if msg.type =='Sharing':
        response = requests.get(msg.url)   
        document = PyQuery(response.text)    
        content = document('#js_content').text()
        list_content = stats_word.stats_text(content,100)
        string_content = ''.join(list_content)
    return '{}'.format(string_content)
embed()


