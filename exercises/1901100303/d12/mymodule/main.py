'''
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


from mymodule import stats_word
from os import path
import json
import re
import logging

import requests
from pyquery import PyQuery
import yagmail

import getpass
sender = input('输⼊入发件⼈人邮箱:')
password = getpass.getpass('输⼊入发件⼈人邮箱密码(可复制粘贴):')
recipients = input('输⼊入收件⼈人邮箱:')

r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(r.text)
content = document('#js_content').text()

wx_list = stats_word.stats_text_cn(content,100)
wx_str =''

for word in wx_list:
    wx_str = wx_str + str(word)

yagmail.SMTP('sender','password').send('pythoncamp@163.com','[1901100303]自学训练营学习20群 day11 yuanweiyu',wx_str)

'''
from wxpy import *
import requests
from pyquery import PyQuery
import yagmail
from mymodule import stats_word

bot = Bot()


#print(my_friend)

def get_msg():
    my_friend = bot.friends().search('冰山',city = '临沂')[0]
    if Message.type = 'Sharing':
        r = requests.get(url)
        document = PyQuery(r.text)
        content = document('#js_content').text()

        return(str(stats_word.stats_text_cn(content,100))

def send_msg():
    try:
        my_friend = bot.friends().search('冰山',city = '临沂')[0]
        my_friend.send(get_msg)
    except:
        pass

if __name__ = '__main__':
    send_msg()








