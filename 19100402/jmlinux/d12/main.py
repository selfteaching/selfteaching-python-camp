from mymodule import stats_word
from pyquery import PyQuery
from wxpy import *
import getpass
import requests

bot = Bot()
my_friend = bot.friends()
#my_friend = bot.friends().search("丽")[0]
#my_friend.send("请发一篇公众号文章给我，我想给些惊喜你看,返回文章前10个高频词给你")
#print("消息发送成功")

@bot.register(my_friend)
def send_result(msg):
    if msg.type == "Sharing":
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        str1 = str(dict(stats_word.stats_text_cn(content,10)))
        print(str1)
        #my_friend.send(str1)

embed()