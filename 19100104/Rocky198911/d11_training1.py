#coding=utf-8
from mymodule import stats_word as sw
from pyquery import PyQuery
import requests
import yagmail
import getpass

sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

document = PyQuery(r.text)
content = document('#js_content').text()
#my_stats = str(sw.stats_text(content, 100))

yag = yagmail.SMTP(user=sender, password=password, host='smtp.163.com')

yag.send(recipients, '19100104 Jacquesxu666', str(sw.stats_text(content, 100)))
