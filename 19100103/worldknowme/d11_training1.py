# -*- coding: utf-8 -*-
import re
import jieba
from collections import Counter
import requests
response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')   #获取微信公众号文章返还结果'response'
from pyquery import PyQuery
document=PyQuery(response.text)       #将内容抓取下来
content=document('#js_content').text()      #获取正文内容

#..........


import getpass                                  #使用getpass获得用户名和密码
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱的密码（可复制粘贴）:')
recipients = input('输入收件人邮箱：')
                  
import stats_word_d11
s = stats_word_d11.stats_text(content,100)        #引用stats.text 来统计100个词
s = str(s)                                        #转为字符串str类型

import yagmail                                              #导入yet another gmail模块
yag = yagmail.SMTP(user=sender,password=password,host='smtp.qq.com')   
title = '19100103 worldknowme'

yag.send(to = recipients, subject = title,contents = s)    #给目标发邮件
yag.send(subject = title,contents = s)                     #给自己发邮件