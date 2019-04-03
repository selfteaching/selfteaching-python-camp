# 导入模块
from wxpy import *
from pyquery import PyQuery
import requests
import stats_word
# 初始化机器人，扫码登陆
bot = Bot()

# 监听好友消息
my_friend = bot.friends()
@bot.register(my_friend)
def reply_my_friend(msg):
# 如果消息为 分享(SHARING)类型，则获取消息的网页链接(msg.ugl)
    if msg.type =='Sharing':    
        response = requests.get(msg.url)  
        document = PyQuery(response.text)   
        content = document('#js_content').text()            
        c= str(stats_word.stats_text(content, 100))
        # 将获得的信息回复好友
        msg.reply(c)
    else:
        pass
    
embed()