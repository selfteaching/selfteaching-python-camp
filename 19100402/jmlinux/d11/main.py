from mymodule import stats_word
from pyquery import PyQuery
import json
import getpass
import yagmail
import requests

sender=input('输入发件人邮箱：')
password=getpass.getpass('输入发件人邮箱密码：')
recipients=input('输入收件人邮箱：')

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()
str1 = str(dict(stats_word.stats_text_cn(content,100)))
#print(content)

email = yagmail.SMTP(sender,password,'smtp.qq.com') 
email.send(recipients,'19100402 jmlinux',str1)