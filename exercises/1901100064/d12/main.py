from mymodule import stats_word
import logging
import jieba
import requests
import pyquery
from wxpy import *


logging.basicConfig(format='file:%(filename)s | line:%(lineno)d | message:%(message)s',\
    level=logging.DEBUG)


# 定义提取微信公众号正文的函数
def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    print(r)
    t =r.text
    #print(t)
    d = pyquery.PyQuery(t)
    #print(d)
    article = d('#js_content').text()
    print(article )
    return article




def main():
    # 导入模块
    # 初始化机器人，扫码登陆
    bot = Bot()
    friends = bot.friends()

    @bot.register(friends,SHARING)
    def handler(msg):
        try:
            logging.info('sharing url = %s',msg.url)
            article=get_article(msg.url)
            result = stats_word.stats_text_cn(article,10)
            msg.reply(str(result))
        except Exception as e:
            #抛出错误
            logging.exception(e)

    # 进入 Python 命令行、让程序保持运行
    embed()


if __name__ == "__main__":
    main()


