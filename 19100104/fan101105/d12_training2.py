
from mymodule import stats_word
import requests
from pyquery import PyQuery
from wxpy import *
'''
import yagmail
import getpass
'''
bot = Bot()
myfriend1 = bot.friends().search('alan')[0]
if myfriend1.Message.type == 'Sharing':
    url = Message.url
    response = requests.get(url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    top100=str((stats_word.stats_txt_cn(content)))
    myfriend1.send(top100)
'''
sender = input('请输入发件人信箱:')
password = getpass.getpass('请输入发件人信箱密码（可复制粘贴）:')
recipients = input('请输入收件人邮箱:')
#链接邮箱服务器
yag = yagmail.SMTP( user=sender, password=password, host='smtp.sohu.com')

# 邮箱正文
contents = top100

# 发送邮件
yag.send(recipients, '19100104 fan101105', contents)
'''



