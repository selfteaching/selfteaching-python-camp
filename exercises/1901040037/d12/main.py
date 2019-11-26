#-*- coding:utf-8 -*-
from mymodule import stats_word
import json
from collections import Counter
import yagmail
import requests
import pyquery
import sys
import getpass

from wxpy import *

def main():
    bot = Bot() #扫描二维码登录微信
    my_friend = bot.friends() #回复对象为所有好友

    @bot.register(my_friend,SHARING) #接受分享类消息

    def auto_reply(msg):
        response = requests.get(msg.url) #msg.url为分享的网址
        document = pyquery.PyQuery(response.text)
        content = document('#js_content').text()
        #处理文本
        result = stats_word.stats_text_cn(content)
        return result

    my_friend.send(auto_reply()) #将结果返回给好友



    embed() #堵塞线程，保持监听状态

if __name__ == '__main__':
    main()