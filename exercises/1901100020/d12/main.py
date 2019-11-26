# 安装微信依赖包 wxpy
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple wxpy
import logging
import requests
import pyquery
from wxpy import *
from mymodule import stats_word

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message: %(message)s', level=logging.DEBUG)
# 提取微信公众号文章正文
def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
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
            result = stats_word.stats_text_cn(article, 100)
            msg.reply(str(result))
        except Exception as e:
            logging.exception(e)
    embed()

if __name__ == "__main__":
#<<<<<<< 1001S02E02_hello_python.py
    main()
#=======
    main()
#>>>>>>> master
