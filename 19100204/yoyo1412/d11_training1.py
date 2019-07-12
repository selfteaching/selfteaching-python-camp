import requests
import yagmail
import getpass
from pyquery import PyQuery 
from D10 import Chinesechar
#sender = input('输入发件人邮箱:')
#password = getpass.getpass('输入发件人邮箱密码:')
#recipients = input('输入收件人邮箱:')
#smtp = 'smtp.163.com'
response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery (response.text)
content = document ('#js_content').text()
statistics = Chinesechar(content,100)

#yagmail.SMTP(sender,password,smtp).send(recipients,'yoyo1412',statistics)
