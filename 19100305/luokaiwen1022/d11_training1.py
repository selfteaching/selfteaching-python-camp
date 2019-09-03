'''这是一个通过网络请求获得网页内容，使用分词工具对中文字符串
进行分词，统计词频，得出结果，并发送到指定邮箱的程序'''
import requests
import pyquery
from pyquery import PyQuery
from mymodule import stats_word

'''访问网址'''
image_url = "https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"
'''将网址中的内容全部赋值给response'''
response = requests.get(image_url)
'''提取网址中的正文内容'''
document = pyquery.PyQuery(response.text)
content = document('#js_content').text()
statList = stats_word.stats_text_cn(content,100)
statstring = ''.join(str(i) for i in statList)


import getpass
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')
recipients = input('输入收件人邮箱：')

import yagmail

yag = yagmail.SMTP(user=sender,password=password,host='smtp.qq.com')


yag.send(recipients,'19100305 luokaiwen1022主题：张小龙微信公开课演讲稿中文词频前100名统计',statstring)