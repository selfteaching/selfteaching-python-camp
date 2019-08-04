# day12 实战应用
# 2019年7月25日
# 陈浩 学号 1901100030

import logging
import yagmail
import requests
import pyquery
import getpass
from mymodule import stats_word
# 导入模块
from wxpy import *


# 初始化logging模块
logging.basicConfig(format="file:%(filename)s|line:%(lineno)d|message:%(message)s",level=logging.DEBUG)

# 获取微信公众号正文
def get_article(url):
    r = requests.get(url)
    document = pyquery.PyQuery(r.text)
    return document("#js_content").text()

def main():
    
    # 初始化机器人，扫码登陆
    bot = Bot()
    friends = bot.friends()

    @bot.register(friends, SHARING)
    def handler(msg):
        try:
            article = get_article(msg.url)
            logging.info("sharing url = %s",msg.url)
            result = stats_word.stats_text_cn(article, 10)
            logging.info("%s %s", type(result), str(result))  
            msg.reply(str(result))     
        except Exception as e:
            logging.exception(e)
        embed()

if __name__ == "__main__":
    main()



