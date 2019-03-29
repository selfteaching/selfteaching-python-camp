import requests
import pyquery
import yagmail
from pyquery import PyQuery
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(r.text)
content = document('#js_content').text()

import getpass
sender = input('输入发件人邮箱')
password = getpass.getpass('输入发件人邮箱密码')
recipients = input('输入收件人邮箱')

from mymodule import stats_word#导入stats_word模块
result = stats_word.stats_text(content,100)
result1 = str(result)
print(result1)

yag = yagmail.SMTP(user = sender,password = password,host = 'smtp.qq.com')
contents = ['这里是内容']
yag.send(to = recipients,subject = '19100101 xiaoguaishou01',contents = result1)