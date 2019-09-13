from mymodule import stats_word
import requests
from pyquery import PyQuery

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
print(response.text)

document = PyQuery(response.text)
content = document('#js_content').text()
print(content)

result = print(stats_word.stats_text_cn(content,100))



import getpass
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码：')
recipients = input('输入收件人邮箱：')

import yagmail
mail = yagmail.SMTP(sender,password,'smtp.qq.com')
subject = '自学训练营学习1群 DAY11 samele0077'
mail.send(to = recipients, subject =subject, contents = result)