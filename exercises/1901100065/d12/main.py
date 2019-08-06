from mymodule import stats_word
import requests
from pyquery import PyQuery
from wxpy import *

def getarticle(url):
    r = requests.get(url)
    document = PyQuery(r.text)
    return document('#js_content').text()

def main():
    bot = Bot()
    my_frinds = bot.friends().search('brian')[0]
    @bot.register(my_frinds)
    def reply_statistic(msg):
        if  msg.type == 'Sharing':
           texturl = msg.url          # 获取分享内容的链接
           text = getarticle(texturl) 
           replay_content = stats_word.stats_text_cn(text, 100)
           msg.reply(replay_content)
            
    embed()



if __name__ == '__main__':
    main()
