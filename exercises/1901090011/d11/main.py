
import requests
from pyquery import PyQuery
#r = requests.get('https://api.github.com/user', auth=('user', 'pass')) 官方示例
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()
from mymodule.stats_word import stats_text as a
list1 = a(content,100)
str_1 = ' '.join(str(i) for i in list1)

import getpass
sender = input('輸入發件人郵箱：')
password = getpass.getpass('輸入發輸入發件人郵箱密碼（可複制粘貼)：')
#When no password is given and the user is not found in the keyring, getpass.getpass() is used to prompt the user for a password. 
recipients = input('輸入收件人郵箱：')
import yagmail
#yagmail.SMTP('mygmailusername').send('to@someone.com', 'subject', 'This is the body')
#yag = yagmail.SMTP('mygmailusername', 'mygmailpassword')
#yag.send('to@someone.com', 'subject', contents)

yag = yagmail.SMTP(user = sender,password = password,host ='smtp.mail.yahoo.com')
yag.send(recipients,'1901090011 DAY11 KHHsieh',contents=str_1)

