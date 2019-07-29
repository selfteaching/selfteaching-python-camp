from models.stats_word_11 import *
# import json

# with open('E:/python/day11/tang300.json', 'r', encoding='utf-8') as file:
#     str = file.read()
#     count=20
#     try:
#         print(f'输出词频最高的前20个汉字词频：{stats_text_cn(str,count)}')
#     except :
#         print('are you sure this is a string')

import requests

from pyquery import PyQuery

response=requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
document = PyQuery(response.text)
content = document('#js_content').text()
#print(content)
count=100
a=str(stats_text(content,count))
print(a)


import getpass
sender = input('输⼊入发件⼈人邮箱:')
password = input('输入密码：')
recipients = '535652072@qq.com'
import yagmail
yag=yagmail.SMTP(user=sender,password=password,host='smtp.126.com')

contents=a
subject='自学营008期01班 xujalg'
yag.send(recipients,subject,contents)