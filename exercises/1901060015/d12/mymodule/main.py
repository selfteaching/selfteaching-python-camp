import requests
from pyquery import PyQuery
import stats_word
import logging
from wxpy import *

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)



#获取url
def get_url(url):
    r = requests.get(url)
    d=PyQuery(r.text)
    return d('#js_content').text().replace("，","").replace("。","").replace("\n","")


def main():
    bot =Bot(cache_path=True)
    my_friend=bot.friends()

    @bot.register(my_friend,SHARING)
    def handler(msg):
        try:
            logging.info('sharing url = %s',msg.url)
            artical =get_url(msg.url)
            result = stats_word.stats_text_cn(artical)
            msg.reply(str(result))
        except Exception as e:
            logging.exception(e)
    embed()

if __name__ == "__main__":
    main()

























