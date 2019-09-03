
import stats_word as sw 
import json
from pyquery import PyQuery
import requests
import yagmail
import getpass


r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(r.text)
text = document('p').text()
contents = str(sw.stats_text_cn(text, 100))


sender = input('输⼊入发件⼈人邮箱:')
password = getpass.getpass('输⼊入发件⼈人邮箱密码(可复制粘贴):')
recipients = input('输⼊入收件⼈人邮箱:')
yag = yagmail.SMTP(sender, password)
yag.send(recipients, '自学训练营学习10群 DAY11 TYcugb', contents)