import requests                 #获取网址
from mymodule import stats_word #统计单词
from wxpy import *

bot = Bot()
friend_M = bot.friends().search("M.")[0]

@bot.register(friend_M,SHARING)
def auto_get_url(msg):
    response = requests.get(msg.url)
    from pyquery import PyQuery as py
    document = py(response.text) 
    content = document('#js_content').text()
    text1 = stats_word.stats_word(content,100)
    text2 = str(text1)
    bot.file_helper.send(text1)
    return text2
    
# 堵塞线程，并进入 Python 命令行
embed()

