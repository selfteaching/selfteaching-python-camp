import json
import stats_word
import jieba
import requests
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
from pyquery import PyQuery
document = PyQuery(response.text) 
content = document('#js_content').text()
import yagmail
import getpass
sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码(可复制粘贴):') 
recipients = input('输入收件人邮箱:')
contents = [str(stats_word.stats_text_cn(content,100))]
subject = '自学训练营学习4群 Day11 Isabelmima'
yagmail.SMTP(sender, password, host = 'smtp.163.com')
yag.send(recipients, subject, contents)
