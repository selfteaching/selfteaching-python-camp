# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:46:48 2019

@author: PetalSaya
"""

import stats_word
import requests


response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text()

result = stats_word.stats_text_cn(content,100)

import getpass
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）: ')
recipients = input('输入收件人邮箱: ')

import yagmail
stmp = 'smtp.gmail.com'
yag = yagmail.SMTP(sender,password,stmp)
yag.send(recipients, '自学训练营学习1群 Day11', result)