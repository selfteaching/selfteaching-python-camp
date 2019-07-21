import yagmail
import requests
from mymodule import stats_word
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

from pyquery import PyQuery as py
document = py(response.text) 
content = document('#js_content').text()

text1 = stats_word.stats_word(content,100)


import getpass
sender = input('请输入发件人邮箱：')
password = getpass.getpass('请输入发件人邮箱密码（可复制粘贴）：')
recipients ='pythoncamp@163.com'       #input('请输入收件人邮箱：')
host = 'smtp.qq.com'

yag = yagmail.SMTP(sender,password,host)
subject1 = '自学训练营学习4群 DAY11 Mgteller'
text2= str(text1)
yag.send(recipients,subject=subject1,contents=text2)
