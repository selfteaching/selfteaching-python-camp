import requests
from pyquery import PyQuery
from mymodule import stats_word
import yagmail




content = str('今天天气真好')

import getpass

sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')
print(sender)
yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com')
print(stats_word.stats_text(content, 10))
print(str(stats_word.stats_text(content,10)))
yag.send(recipients, '19100305 luyingyi ', str(stats_word.stats_text(content, 10))) 