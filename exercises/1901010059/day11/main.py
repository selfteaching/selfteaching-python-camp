

import requests
from pyquery import PyQuery
#r = requests.get('https://api.github.com/user', auth=('user', 'pass')) 官方事例
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()
from mymodule.stats_word import stats_text as a
list1 = a(content,100)
str_1 = ' '.join(str(i) for i in list1)

import getpass
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')
#When no password is given and the user is not found in the keyring, getpass.getpass() is used to prompt the user for a password. 
recipients = input('输入收件人邮箱：')
import yagmail
#yagmail.SMTP('mygmailusername').send('to@someone.com', 'subject', 'This is the body')
#yag = yagmail.SMTP('mygmailusername', 'mygmailpassword')
#yag.send('to@someone.com', 'subject', contents)

yag = yagmail.SMTP(user = sender,password = password,host ='smtp.qq.com')
yag.send(recipients,'1901010059 DAY11 shannoxu',contents=str_1)

