import stats_word
import os
import yagmail
import requests
import pyquery

#获取微信公众号文章返还结果'response'
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

from pyquery import PyQuery
#完成内容抓取
document = PyQuery(r.text)
#正文内容获取
content = document('#js_content').text()

#对内容进行str类型转换
tongji = stats_word.stats_text_cn(content,100)
str_zxl = str(tongji)

import getpass
sender = input('输入发件⼈邮箱:')
password = getpass.getpass('输入发件⼈邮箱密码(可复制粘贴):')
recipients = input('输入收件⼈邮箱:')

yag = yagmail.SMTP(user = sender, password = password, host = 'smtp.126.com')  
#发送邮件
yag.send(recipients,'自学训练营学习4群，github：Konaair，day11',str_zxl)