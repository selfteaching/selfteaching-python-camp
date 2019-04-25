import requests
from pyquery import PyQuery
import sys
sys.path.append("/Users/zhangdequan/Documents/GitHub/selfteaching-python-camp/19100302/DequanZhang/mymodule")
from stats_word import stats_text_cn

#使用requests请求微信公众号文章链接，获取返回结果（response）
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()

# 通过yagmail登陆自己的邮箱，发送统计结果到pythoncamp@163.com
import yagmail
import getpass
sender = input('输入发件人邮箱：')   
password = getpass.getpass('输入发件人邮箱密码：')
recipients = input('输入收件人邮箱：')

statlist=stats_text_cn(content,100)
statstring=''.join(str(i) for i in statlist)

yag = yagmail.SMTP(sender, password, 'smtp.okstate.edu')
subject = '19100302 DequanZhang'
yag.send(to = recipients, subject = subject, contents = statstring)

print('发送邮件成功') 