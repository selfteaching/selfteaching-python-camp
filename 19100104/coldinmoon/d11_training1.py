#1.使用requests请求微信公众号链接，获取返回结果
#2.将response.text用pyquery把微信公众号正文提取出来
#3.使用stats_word中stats_text_cn分析统计前100词频结果
#4.通过yag登录邮箱，发送统计结果
#Date:3/28/2019

#使用requests请求微信公众号链接，获取返回结果
import requests

response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

#将response.text用pyquery把微信公众号正文提取出来
from pyquery import PyQuery as pq

document=pq(response.text)
content=document('#js_content').text()

#设置输入邮箱、密码、收件人
import getpass

sender=input('请输入发件人邮箱：')
password=getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')
recipients=input('请输入收件人邮箱：')

#使用stats_word中stats_text_cn分析统计前100词频结果
from mymodule.stats_word import stats_text_cn as stc

result=stc(content,100)
result=str(result)

#通过yag登录邮箱，发送统计结果
import yagmail

yag=yagmail.SMTP(user=sender,password=password,host='smtp.qq.com')

yag.send=(recipients,'19100104 coldinmoon',result)