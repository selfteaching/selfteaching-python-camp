from mymodule import stats_word
import jieba
import re
import requests
response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
import getpass 
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人授权码：')
recipients = input('输入收件人邮箱：')
from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text()
freq=stats_word.stats_txt(content,100)
freq=str(freq)
import yagmail
yag=yagmail.SMTP(sender,password,'smtp.163.com')
yag.send(to=recipients,subject = '19100402 Wangzhebin',contents = freq)