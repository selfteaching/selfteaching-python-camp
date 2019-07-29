#'''这是一个通过网络请求获得网页内容，使用分词工具对中文字符串
#进行分词，统计词频，得出结果，并发送到指定邮箱的程序'''
import requests
import pyquery
from pyquery import PyQuery
from mymodule import stats_word

#'''访问网址'''
image_url = "https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"
#'''将网址中的内容全部赋值给response'''
response = requests.get(image_url)
#'''提取网址中的正文内容'''
document = pyquery.PyQuery(response.text) #抓取文字信息
content = document('#js_content').text() #把抓取的内容写成可视的文字
import getpass
sender = input('输入发件人邮箱:')
password = getpass.getpass('输入邮箱密码:')
recipients = input('pythoncamp@163.com')

import yagmail
yag = yagmail.SMTP(user=sender,password=password,host='smtp.163.com')
yag.send(recipient,'19100205 zd14202')