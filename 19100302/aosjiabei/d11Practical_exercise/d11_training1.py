from pyquery import PyQuery
import yagmail
import smtplib
import requests
#提取公众号正文
response= requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')    # 最基本的GET请求
document = PyQuery(response.text) 
content = document('#js_content').text()

#统计中文词频
from stats_word_d11 import stats_text_cn
result=str(stats_text_cn(content))

#用yag发邮件
sender =input("please input sender email:") 
pwd =input("please input sender password:")
receiver =input("please input receiver email:") 
host1 = "smtp.163.com"  # 设置发件服务器地址
port = 465 # 设置发件服务器端口号。
title = "19100302 aosjiabei"

try:
	yag = yagmail.SMTP(user=sender,password=pwd,host=host1)   
	yag.send(to = receiver, subject = title,contents = result)   
	yag.send(subject = title,contents = result)                  #给自己发用于验证
	print ('Well Done')
except smtplib.SMTPException:
	print ('Error')
