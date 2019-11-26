from mymodule import stats_word
from wxpy import Bot, Message, embed
from pyquery import PyQuery
import requests

bot = Bot()   # 初始化机器人，扫码登录
my_friend = bot.friends().search('闫')[0]    # 查找好友
my_friend.send('分享任意微信文章给我')   # 发生文本给好友

# 监听消息
# 回复好友消息
@bot.register(my_friend)
def reply_my_friend(msg):
    if msg.type == 'Sharing':
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        reply = stats_word.stats_text_cn(content, 100)
    return reply
embed()


path = r'd:\用户目录\我的文档\GitHub\selfteaching-python-camp\exercises\1901010161\d11\mymodule\tang300.json'
with open(path, 'r', encoding='UTF-8') as f:     # byte编码的类型名称是 UTF-8
    read_date = f.read()


try:
    print('出现频率最高的前20个词： \n', stats_word.stats_text_cn(read_date, 20))
except ValueError:
    print('ValueError:type of argument is not string!')
