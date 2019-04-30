import requests
from pyquery import PyQuery
import getpass
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码：')
recipients = input('输入收件人邮箱：')
url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
response = requests.get(url)
document = PyQuery(response.text)
content = document('#js_content').text()

import stats_word
count = 100

contents = stats_word.stats_text(content,count)

result = contents.__str__()

import yagmail

yag = yagmail.SMTP(user=sender,password=password,host='smtp.qq.com')

yag.send(recipients,'19100204+jinzhijian77',result)