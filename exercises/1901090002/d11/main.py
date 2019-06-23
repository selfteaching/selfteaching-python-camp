from mymodule.stats_word import *
from pyquery import PyQuery as pq
from lxml import etree
import urllib
import requests
import yagmail
import getpass

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = pq(response.text)
content = document('#js_content').text()
print(stats_text_cn(content,100))


to = 'pythoncamp@163.com'
subject = '【自学营008期01班】自学训练营 DAY11 yuxudng2018'
a = stats_text_cn(content,100)
body=str(a)

sender = input('输入发件人邮箱')
password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')

yag=yagmail.SMTP(user=sender, password=password, host='smtp.163.com')
yag.send(to, subject,body)