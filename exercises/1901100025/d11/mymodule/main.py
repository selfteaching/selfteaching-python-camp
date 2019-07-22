from stats_word import stats_text_cn
import yagmail
import requests
from pyquery import PyQuery
import getpass
sender = input('请输入发件人邮箱：')
password = getpass.getpass('Please input your password: ')
recipients= input('请输入收件人邮箱：')
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()
words = str(stats_text_cn(content))
yag = yagmail.SMTP(sender, password, 'smtp.163.com')
yag.send(recipients, '[1901100025]自学营009期DAY11 Sweetwisefeather', words)
