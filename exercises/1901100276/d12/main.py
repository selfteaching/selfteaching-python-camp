from mymodule import stats_word
import  yagmail
import  requests
import pyquery
import getpass
from wxpy import *
from pyquery import PyQuery
bot=Bot(cache_path=True)    #缓存登录
myfriend = bot.friends().search(u'陈陈醋醋')[0]     #监控好友消息
@bot.register(myfriend,SHARING)     #寻找好友分享类消息

def get_friend(msg):
    if isinstance(msg.type,SHARING):
        response=requests.get(msg.url)#获取链接

        document = PyQuery(response.text)

        content= document('#js_content').text()
    
        result = stats_word.stats_text(content,100) 
        msg.reply(str(result))
embed()