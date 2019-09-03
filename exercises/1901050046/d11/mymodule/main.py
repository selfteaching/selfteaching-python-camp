#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import yagmail
import getpass
import requests
import stats_word
from pyquery import PyQuery

#提取文章正文
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(r.text)
content = document('#js_content').text()
#统计词频
result = stats_word.stats_text_cn(content,100,len_size = 2)
result_str = ""
for i in result:
    result_str += str(i)
print("统计结果为：", result_str)

#配置邮箱
sender = input("输入发件人邮箱：")
password = getpass.getpass('输入发件人邮箱密码：')
recipients = input('输入收件人邮箱：')
#链接邮箱服务器
yag = yagmail.SMTP( user= sender, password=password, host='smtp.sina.cn')
# 邮箱正文
contents = result_str
# 发送邮件
yag.send(recipients, '自学训练营学习4群 DAY11 sixthspace', contents)





