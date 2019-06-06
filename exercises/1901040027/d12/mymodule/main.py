
import requests
from pyquery import PyQuery
import stats_word
from wxpy import *
#初始化机器人，扫码登陆
bot = Bot()
#找到好友
my_friend = bot.friends().search('小企鹅1')[0]
#发送文本给好友
my_friend.send('程序测试，转发任意微信推文给我，完成测试')
#监听消息
@bot.register()
def print_others(msg):
        print(msg)
#回复my_friend的消息
@bot.register(my_friend)
def reply_my_friend(msg):
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        reply = stats_word.stats_text_cn(content)
        return reply

embed()


