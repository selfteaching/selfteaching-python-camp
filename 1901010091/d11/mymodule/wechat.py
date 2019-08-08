import getpass
user=input('输入发件人邮箱:')
password=getpass.getpass('输入发件人邮箱密码:')

import requests  
url ="https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"
response = requests.get(url)
response.encoding = "utf-8"

from pyquery import PyQuery
document = PyQuery(response.text) 
content = document('#js_content').text()

count=100
import stats_word
try:
    stats_word.stats_text(content,count)
except ValueError:
    print("文本为非字符串")

cn=stats_word.stats_text_cn.textout
ttt=str(cn)

import yagmail
yag=yagmail.SMTP(user,password,host='smtp.sina.com')
yag.send(to='pathoncamp@163.com',subject='自学训练营学习2群DAY11 Andy910',contents=ttt)

