import requests
import pyquery
import yagmail
import getpass
import stats_word

from pyquery import PyQuery

response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document=PyQuery(response.text)
content=document('#js_content').text()

text=stats_word.stats_text_cn(content,100)
text1=str(text)

addresser=input('输入发件人邮箱：')
password=getpass.getpass('输入发件人邮箱密码：')
recipients=input('输入收件人邮箱：')

yag=yagmail.SMTP(addresser,password,'smtp.126.com')
yag.send(recipients,'自学训练营学习1群 DAY11 canielhy',text1)
