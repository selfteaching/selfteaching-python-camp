import requests
from pyquery import PyQuery
import mymodule.stats_word

from wxpy import *
bot = Bot()

my_friend = bot.friends().search('权')[0]    # 找到好友
my_friend.send('send me something')    # 发送消息给这个好友

@bot.register(my_friend)
def reply_my_friend(msg):
    print(msg)
    if msg.type =='Sharing':    # 如果是公众号内容进行统计词频处理
        response = requests.get(msg.url)    # 请求获得内容
        document = PyQuery(response.text)    # 解析提出内容
        content = document('#js_content').text()
        print(content)
        result = str(mymodule.stats_word.stats_text_cn(content))    # 导入公式处理结果
        my_friend.send(result)    # 结果发送给好友
    else:
        pass
    
embed()    # 让程序保持运行