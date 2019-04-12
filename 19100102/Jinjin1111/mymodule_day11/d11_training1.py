import yagmail
import requests
import pyquery
import stats_word
import sys
import getpass


# r=requests.get('https://api.github.com/uder',auth=('user','pass'))
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)
# print(r.json())

#提取微信公众号文章正文
r=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA',auth=('user','pass'))
document=pyquery.PyQuery(r.text)
content=document('#js_content').text()

#调用stats_word中的stats_text_cn函数统计词频
mdict=[]
strResult=''
try:
    mdict=stats_word.stats_text_cn(content,100)
except:
    print("error:",sys.exc_info()[0])

strResult=','.join([str(x) for x in mdict])
#strResult='test'

#发送邮件
sender=input('请输入发件人邮箱：')
password=getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')
recipients=input('请输入收件人邮箱：')

try:
    yag=yagmail.SMTP(sender,password,'smtp.mail.aliyun.com')
    #yag.send('pythoncamp@163.com','subject',strResult)
    yag.send(recipients,'19100102 Jinjin1111',strResult)
    print("已发送，请注意查收。")
except:
    print("error:",sys.exc_info()[0])