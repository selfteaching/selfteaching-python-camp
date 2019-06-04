from mymodule import stats_word 
import  requests
from pyquery import PyQuery
from wxpy import *

#初始化机器人，扫码登录
bot = Bot() 

# 找到好友并发消息
my_friends = bot.friends().search('慧子')[0]
my_friends.send('请给我分享一篇公众号文章')

# 获取文章url
@bot.register(my_friends,SHARING)
def get_msg (msg) :
    #使用requests获得获得网络链接的文本
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
    #将获得的文章进行分词
        text = str(dict(stats_word.stats_text_cn(content,100)))
    #给好友发送信息
        my_friends.send(text)
#让程序保持运行
embed()

