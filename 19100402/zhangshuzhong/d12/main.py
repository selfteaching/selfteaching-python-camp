import requests
import pyquery
import yagmail
import getpass
from mymodule import stats_word
from pyquery import PyQuery
#导入模块
from wxpy import *
#初始化机器人，扫码登录
bot = Bot()
#搜索名称含有“张书忠”的好友
my_friends=bot.friends().search('张书忠')[0]
#给好友发送信息
#my_friends.send('你好')


#监听好友消息
#通过装饰器，注册一个接收制定好友分享消息的函数
@bot.register(my_friends,SHARING)
def friend_sharing(msg):
    #获得分享内容的网络链接
    dizhi=msg.url
    #使用requests获得获得网络链接的文本
    response = requests.get(dizhi)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    #将获得的文章进行分词
    text = stats_word.stats_text_cn(content,100)
    text1 = str(text)
    #给好友发送信息
    my_friends.send(text1)
#让程序保持运行
embed()