from mymodule import stats_word
from os import path
import requests
from pyquery import PyQuery
import yagmail
import getpass
import logging

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA',verify=False)

document = PyQuery(response.text)

content = document('#js_content').text()

result = stats_word.stats_text_cn(content,100)

result = str(result)  

print('result',result)



sender = input('输入发件人邮箱:')

password = getpass.getpass('输入发件人邮箱密码(可复制粘贴):')

host = "smtp.126.com"  # SMTP服务器地址

yag = yagmail.SMTP(sender,password,host)



recipients = input('输入收件人邮箱:')  

subject = '自学训练营学习7群 DAY11 贾潇斌 '

yag.send(recipients,subject,result)   # 收件人，主题，正文



print('发送完成')


