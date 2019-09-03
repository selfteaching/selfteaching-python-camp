# 整理数据
import requests
from pyquery import PyQuery
from stats_word import stats_text_cn

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()
stats = stats_text_cn(content,100)
# 发送邮件
import yagmail
import getpass

sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')
yag = yagmail.SMTP(sender,password,'smtp.qq.com')
contents = str(stats)
yag.send(recipients, '19100301 Xuzhengfu', contents)