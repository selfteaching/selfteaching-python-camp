#coding: utf-8  
# 2019.03.28
import requests
from pyquery import PyQuery

# 1.访问url
w_url='https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
response = requests.get(w_url)

# 2.提取微信公众号正文
document = PyQuery(response.text)
content = document('#js_content').text()#把抓取的内容写成可视的文字，#js_content是格式转换?

from mymodule import stats_word
# 3.统计前100词频
statList = stats_word.stats_text(content, 100)
statString = ''.join(str(i) for i in statList)

import yagmail
import getpass
# 4.设置发件人、登录密码、收件人
sender = input('请输入发件人邮箱：')
psw = input('请输入发件人邮箱登录密码：')
recipients = input('请输入收件人邮箱：')
smtp = 'smtp.yeah.net'

# 5.将统计结果发送到 pythoncamp@163.com
yagmail.SMTP(sender, psw, smtp).send(recipients, '19100101 zhwycsz', statString)

