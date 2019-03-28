# -*- coding: utf-8 -*-

#导入外部库
import requests



response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

from pyquery import PyQuery
document = PyQuery(response.text)       #将内容抓取下来
content = document('#js_content').text()        #转换成内容文字,content就是我们得到的结果


import getpass
sender = input('please type send user email:')
password = getpass.getpass('please type password:')
recipients = input('please type recieve user email:')
sever = 'smtp.163.com'

import mymodule.stats_word

result = mymodule.stats_word.stats_text(content,100)
result = str(result)
print(result)

import yagmail
yag = yagmail.SMTP(user=sender,password=password,host=sever)
title = '19100105 slona-song'

yag.send(to = recipients, subject = title,contents = result)
yag.send(subject = title,contents = result)