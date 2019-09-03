from mymodule import stats_word as sw
import requests
from pyquery import PyQuery
from wxpy import *

# 扫描二维码登陆微信 #issue1195 avoiding scanning again shortly
bot = Bot(cache_path=True)

@bot.register()
def auto_reply(msg):
    if msg.type == SHARING:
        response = requests.get(msg.url)  # msg.url为分享的网址
        document = PyQuery(response.text)
        content = document('#js_content').text()
        # 像d11一样处理文本
        result = sw.stats_text_cn(content, count=10)
        # seems better str this type in case causing trouble in reading
        wechat_word = ''.join(str(i)for i in result)
        msg.reply(wechat_word)  # 将结果返回给好友

# embed()
bot.join()
