import stats_word
import logging
import yagmail
import requests
import pyquery
from pyquery import PyQuery
import getpass


resp= requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(resp.text) 
content = document('#js_content').text()

result=stats_word.stats_text_cn(content,100)
result1=str(result)
print(result1)

sender = input('输⼊入发件⼈人邮箱:')
password = getpass.getpass('输⼊入发件⼈人邮箱密码(可复制粘贴):') 
recipients = input('输⼊入收件人邮箱:')

yag = yagmail.SMTP(sender,password, 'smtp.qq.com')
yag.send(recipients, '自学训练营17群 DAY11 Evie-Li',result1)
