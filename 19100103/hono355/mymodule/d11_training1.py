from collections import Counter
import jieba
import pyquery
import requests
import yagmail
import getpass


r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
r.text
from pyquery import PyQuery
document = PyQuery(r.text)
content = document('#js_content').text()
import stats_word1
result = stats_word1.stats_text_cn(content, 100)
result_str =  ' '.join([ str(i) for i in result ])

sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')
title = input('输入标题:')
yag = yagmail.SMTP(sender,password,'smtp.126.com')
yag.send(to = recipients, subject = title, contents = result_str)



