from wxpy import *
import requests
from pyquery import PyQuery
import stats_word

bot = Bot()
my_friend=bot.friends().search("妈")[0]
my_friend.send("send me a message")
@bot.register(my_friend,SHARING)
def my_friend_sharing(msg):
    msg=msg.url
    r = requests.get(msg)
    document=PyQuery(r.text)
    content = document('#js_content').text()
    a=stats_word.stats_text(content,100)
    b=str(a)
    my_friend.send(b)

embed()
# 进入 Python 命令行、让程序保持运行


