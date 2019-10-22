import requests
from pyquery import PyQuery
from mymodule import stats_word
from wxpy import Bot,Message,embed
#初始化机器人，扫码登陆
bot = Bot()
#找到好友
my_friend = bot.friends().search('PrincessAKing')[0]
#发送文本给好友
my_friend.send('分享任意微信文章给我')
#监听消息
#回复my_friend的消息
@bot.register(my_friend)
def reply_my_friend(msg):
    if msg.type == 'Sharing':
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        reply = stats_word.stats_text_cn(content,100)
        return reply 
embed()
