import requests
from pyquery import PyQuery
from mymodule import stats_word
import re

#请求链接，获取结果
response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
response.text

#提取正文
document=PyQuery(response.text)
content=document('#js_content').text()

#对提取结果进行分析和统计
a=stats_word.stats_text_cn(content,100)
b=str(a)

#发送邮件
import getpass
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱：')

import yagmail
yag=yagmail.SMTP(sender,password,host='smtp.qq.com')
yag.send(recipients,'自学训练营DAY11 zhupengfei',b)
print('发送成功')