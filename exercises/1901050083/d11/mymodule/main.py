import stats_word
import json
from os import path
import requests
from pyquery import PyQuery
import yagmail

 
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()

# print(content)


count=20

aaaaa=stats_word.stats_text_cn(content, count)
bbbbb=str(aaaaa)
try:
    print(bbbbb)
except ValueError as fnf_error:
        print(fnf_error)

import getpass
sender = input('输入发件人qq邮箱:')
password = getpass.getpass('输入发件人邮箱木马（可复制黏贴）:')
recipients = input('输入收件人邮箱:')

yag = yagmail.SMTP( user=sender, password=password, host='smtp.qq.com')
yag.send(recipients, '自学训练营学习7群 day11 sunanchn', bbbbb)