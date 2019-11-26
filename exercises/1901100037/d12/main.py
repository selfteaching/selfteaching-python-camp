import logging
import requests
import pyquery
from wxpy import *
from mymodule import stats_word

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)

def get_article(ur1):
    r = requests.get(ur1)
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()

def main():
    bot = Bot()
    friends = bot.friends()

    @bot.register(friends,SHARING)
    def handler(msg):
        try:
            logging.info('sharing ur1 = %s',msg.ur1)
            article = get_article(msg.ur1)
            result = stats_word.stats_text_cn(article,100)
            msg.reply(str(result))
        except Exception as e:
            logging.exception(e)
    embed()
  
if __name__ == "__main__":
    main()
