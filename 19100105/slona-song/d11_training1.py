# -*- coding: utf-8 -*-

#导入外部库
import requests



response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

from pyquery import PyQuery
document = PyQuery(response.text)       #将内容抓取下来
content = document('#js_content').text()        #转换成内容文字,content就是我们得到的结果


import getpass                                  #使用getpass获得用户名和密码
sender = input('please type send user email:')
password = getpass.getpass('please type password:')
recipients = input('please type recieve user email:')
sever = 'smtp.163.com'                          #使用的服务器

import mymodule.stats_word                      #运行检索模块

result = mymodule.stats_word.stats_text(content,100)        #输入参数
result = str(result)                                        #转字符串
#print(result)

import yagmail                                              #导入yet another gmail模块
yag = yagmail.SMTP(user=sender,password=password,host=sever)    #没有用register,直接输参数
title = '19100105 slona-song'

yag.send(to = recipients, subject = title,contents = result)    #给目标发邮件
yag.send(subject = title,contents = result)                     #给自己发邮件