#!/usr/bin/python3
import sys
sys.path.append(r"C:\Users\ZGY\Documents\GitHub\selfteaching-python-camp\19100402\zhengguanya\d11")
import mymodule



import json
import jieba

import yagmail
import getpass

sender = input(("输入发件人邮箱:"))
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')

import requests
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
from pyquery import PyQuery
document = PyQuery(r.text)
content = document('#js_content').text()

from mymodule import stats_word
try:
    stats = mymodule.stats_word.stats_text_cn(content)
except ValueError:
    print("ValueError: You have an input that is not a string.")
else:
    print(stats)

yag = yagmail.SMTP(sender,password,'smtp.qq.com')
contents = str(stats)
yag.send(recipients, '19100402 ZhengGuanya', contents)






