#!/usr/bin/python3

import json
import jieba
import requests
import logging
logging.captureWarnings(True)
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA',verify=False)
print(r.status_code)

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
import yagmail
import getpass

sender = input(("输入发件人邮箱:"))
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')
yag = yagmail.SMTP(sender,password,'smtp.qq.com')
contents = str(stats)
yag.send(recipients, '19100402 ZhengGuanya', contents)






