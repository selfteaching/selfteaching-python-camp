import logging
import requests
import pyquery
from wxpy import *
from mymodule import stats_word

# 安装依赖包 wxpy
# pip install -i  https://pypi.tuna.tsinghua.edu.cn/simple  wxpy 

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message: %(message)s', level=logging.DEBUG)

# 提取公众号文章正文
def get_article(url):
    r = requests.get(url)
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()


def main():
    bot = Bot()
    friends = bot.friends()
    @bot.register(friends, SHARING)
    def handler(msg):
        try:
            logging.info('sharing url = %s', msg.url)
            article = get_article(msg.url)
            result = stats_word.stats_text_cn(article,100)
            msg.reply(str(result))
        except Exception as e:
            logging.exception(e)
    embed()

if __name__ == "__main__":
    main()