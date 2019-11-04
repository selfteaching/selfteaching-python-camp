# 先导入第三方库
import requests
from mymodule import stats_word
from pyquery import PyQuery
from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot()
# 搜索名称含有 "三月" 的男性合肥好友
my_friend = bot.friends().search('三月', sex=MALE, city="合肥")[0]
# 发送文本给好友
my_friend.send('分享任意微信文章给我')
# 回复 my_friend 的消息
@bot.register(my_friend)
def reply_my_friend(msg):
    if msg.type == 'Sharing':
        response = requests.get(msg.url) #获取该网页内容
        document = PyQuery(response.text) 
        content = document('#js_content').text() #将网页内容转换成文本
        return stats_word.stats_text_cn(content, 100)
embed()