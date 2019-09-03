import sys
sys.path.append('/anaconda3/lib/python3.7/site-packages')
from mymodule import stats_word
import json
import requests
import pyquery
import yagmail
import getpass
from pyquery import PyQuery

response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document=PyQuery(response.text)
content=document('#js_content').text()

text=stats_word.stats_text_cn(content,100)
text1=str(text)

addresser=input('请输入发件人邮箱：')
password=getpass.getpass('请输入密码：')
receiver=input('请输入收件人邮箱：')

yag=yagmail.SMTP(addresser,password,'smtp.163.com')
yag.send(receiver,'19100402 崔彤彤',text1)

