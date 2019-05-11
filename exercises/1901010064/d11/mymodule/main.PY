import requests
import stats_word
r = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")

from pyquery import PyQuery
document=PyQuery(r.text)
content = document('#js_content').text()

import getpass
sender = input("输入发件人邮箱：")
password = getpass.getpass("输入发件人邮箱密码:")
recipients = input("输入收件人邮箱:")


a=stats_word.stats_text(content,100)
b=str(a)

import yagmail
yag=yagmail.SMTP(sender,password,'smtp.qq.com')
yag.send(recipients,"自学训练营学习1群day11zhanghuijie",b)