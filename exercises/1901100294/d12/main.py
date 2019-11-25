from mymodule import stats_word
import requests
from pyquery import PyQuery
import getpass
import yagmail
from wxpy import *

bot = Bot(cache_path=True)

@bot.register(msg_types=SHARING)
def get_article(Message):
    real_url = Message.url
    r = requests.get(real_url)
    document = PyQuery(r.text)
    article_str = document('#js_content').text()
    result = stats_word.stats_text_cn(article_str, 10)
    return result  #在被注册函数中，可以通过直接 return <回复内容> 的方式来回复消息
    







content = get_article()
