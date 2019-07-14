import requests
import stats_word
import pyquery
import getpass
import yagmail
import logging
from wxpy import *

logging.basicConfig(format='file:%(filename)s[line:%(lineno)d]message:%(message)s',level=logging.DEBUG)

#提取公众号正文
def get_article(url):
    r = requests.get(url)
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()


def main():
    # 初始化机器人，扫码登陆
    bot = Bot()
    friends = bot.friends()

    @bot.register(friends,SHARING)
    def hander(msg):
        try:
            logging.info('sharing - %s',msg.url)
            article = get_article(msg.url)
            result=stats_word.stats_text_cn(article,100)
            #调用stats_word.py文件中的stats_text_cn函数实现：把提取到的文本分词降序排序
            msg.reply(str(result))
        except Exception as e:
            logging.exception(e)

if __name__=="__main__": 
    main()