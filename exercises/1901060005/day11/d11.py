import yagmail
import getpass
import requests
from mymodule import d11_stats_word as sw

sender = input('Please input sender mailaddress:')
password = getpass.getpass('Please input sender mailcode:')
recipients = input('Please input recipients addresses:')


# 提取微信公众号正文
from pyquery import PyQuery
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()
statString = str(sw.stats_text(content,100))

print('sender =', sender, 'password =', len(password), 'recipients =', recipients)
yag = yagmail.SMTP(sender, password, host='smtp.163.com')
yag.send(recipients, '自学营5群 zhiguodavid', statString)
