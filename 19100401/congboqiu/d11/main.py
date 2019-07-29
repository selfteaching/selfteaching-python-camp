import re
import sys
import jieba
import getpass
import yagmail


import requests
from pyquery import PyQuery
from mymodule import stats_word

#爬网页内容，分词，转换字符串
response = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
document = PyQuery(response.text)
content = document('#js_content').text()
#print(content)
text=content
#print(stats_word.stats_text_cn(text,100))
str_text=str(stats_word.stats_text_cn(text,100))

#yagmail邮箱设置
import smtplib
sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')

# 调用yagmail库发送邮件
yag = yagmail.SMTP(sender,password, host='smtp.qq.com')
yag.send(recipients,'19100401 congboqiu',str_text) 



#请输入发件人邮箱:276811842@qq.com
#请输入发件人密码:填写smtp授权码
#请输入收件人邮箱:pythoncamp@163.com
#ocuqoisenxfebgcj
