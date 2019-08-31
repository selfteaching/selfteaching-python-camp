# coding=utf8
#!/usr/bin/python
from wxpy import *
import sys
from pyquery import PyQuery
sys.path.append('/Users/Yang/GitHub:PJ1/selfteaching-python-camp/exercises/1901010120/d11/mymodule/')
from stats_word import stats_text
from os import path

#注册机器人
wechat_bot = Bot()
#注册内容是分享就抽取
@wechat_bot.register(chats=User, msg_types=SHARING)
def process_url(msg):
    content_url = msg.url
    html_code = requests.get(content_url).text
    document = PyQuery(html_code)
    content = document("#js_content").text().replace("\n", "")

    try:
        en_result, cn_result = stats_text("", content)
        # print(cn_result)
        msg.reply(cn_result)

    except ValueError as e:
        print("Exception catched.")
        print(e)

embed()
