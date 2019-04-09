import requests
from pyquery import PyQuery
import getpass
import yagmail
from mymodule import stats_word

#获取公众号的全部response
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
doc = PyQuery(r.text)

#筛选所有包含内容的response
data = str(doc('p'))

#编辑邮件的发送信息
sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:') 
recipients = input('输入收件人邮箱:')

#链接邮箱服务器
yag = yagmail.SMTP(user=sender, password=password, host='smtp.mxhichina.com')

# 将处理的内容转换成邮箱正文
contents = str(stats_text_cn_jieba(data,100))

# 发送邮件
yag.send(recipients, '19100305 lilyteddy', contents)
