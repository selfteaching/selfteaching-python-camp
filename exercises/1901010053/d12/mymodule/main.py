
import requests
import pyquery
import yagmail
import getpass
from pyquery import PyQuery
import stats_word
from wxpy import *

bot = Bot()#扫码登陆微信
my_friends=bot.friends().search('蓝溪')[0]#搜索名称含有“蓝溪”的好友
#给好友发送信息
#my_friends.send('你好')

#监听好友消息
#通过装饰器，注册一个接收制定好友分享消息的函数
@bot.register(my_friends,SHARING)
def friend_sharing(msg):
    #使用requests获得获得网络链接的文本
    address=msg.url
    response=requests.get(address)
    document=PyQuery(response.text)
    content=document('#js_content').text()
    #将获得的文章进行分词
    text = stats_word.stats_text_cn(content,100)
    text1 = str(text)
    #给好友发送信息
    my_friends.send(text1)
#让程序保持运行
embed()