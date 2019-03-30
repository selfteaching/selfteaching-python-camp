import requests
from pyquery import PyQuery
import mymodule.stats_word

from wxpy import *
bot = Bot()

my_friend = bot.friends().search('yourfriend', sex=MALE, city="深圳")[0]
my_friend.send('send me something')

@bot.register(my_friend)
def print_others(msg):
    print(msg)
    if msg.type =='sharing':
        response = requests.get('msg.url')    # 请求获得内容
        
        document = PyQuery(response.text)    # 解析提出内容
        content = document('#js_content').text()
        #print(content)
        result = str(mymodule.stats_word.stats_text(content))    # 导入公式处理结果
        my_friend.send(result)

embed()    # 让程序保持运行