import requests
from pyquery import PyQuery
from mymodule import stats_word
import yagmail



response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

document = PyQuery(response.text) 
content = document('#js_content').text()

import getpass

sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')

yag = yagmail.SMTP(user=sender, password=password, host='smtp.yeah.net')

yag.send(recipients, '19100201 wiltonwung ', str(stats_word.stats_text(content, 100)))