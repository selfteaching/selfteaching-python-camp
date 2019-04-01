import yagmail
import getpass
import requests
from pyquery import PyQuery

# -*- coding: utf-8 -*-
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA', auth=('zoroya@126.com', 'ZoroYa11661246'))

#提取公众号伪代码

document = PyQuery(response.text)
content = document('#js_content').text() #把抓取的内容写成可视的文字



#链接邮箱服务器
sender = input('输入发件人地址:')
password = getpass.getpass('输入发件人密码:')
recipients = input('输入收件人地址:')
smtp = 'smtp.126.com' #服务器地址
#Todo：在下面实现自己的分词统计和发送邮件的操作

#统计内容的前100词频
print(mymodule.stats_word.stats_text(text))


# 发送邮件
yag.send('11661246@qq.com', '19100205 11661246', text)