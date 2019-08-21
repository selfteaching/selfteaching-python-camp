#Selfteaching day11 homework ,email-practice!html-practice!

from mymodule import stats_word as counts  #import module stats_word.py function
   
import requests #调用requests 函数
r=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA') #从微信公众号取内容
r.encoding   #text 格式编码'utf-8'
r.text
response =r.text   #返回文档

from pyquery import PyQuery  #调用网页解释函数
document = PyQuery(response)
text = document('#js_content').text()

from mymodule import stats_word as counts  #import module stats_word.py function

l1=counts.stats_text_cn(text,100) #输出词频TOP 100的词语

stats_string_resut=''.join(str(i)for i in l1) #以字符串输出统计结果 
print('张小龙演讲Top 100高频词',stats_string_resut)

import getpass #调用邮件接入模块，保障密码安全
sender=input('请输入发件人邮箱：')
password=getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')
recipients=input('请输入收件人邮箱：')

import yagmail  #调用邮件接入模块，保障密码安全
yag=yagmail.SMTP(sender,password,'smtp.139.com') #user=sender,password=password,host='smtp.139.com'
yag.send(recipients,'自学训练营学习群4群 day11 homework by GD139',stats_string_resut) #send to 'pythoncamp@163.com',subject='',contents=''

#yag.send('pythoncamp@163.com','自学训练营学习群4群 GD139',stats_string_resut)
#yag.send() #send none to yourself
#yag.send(subject = 'to self', contents = 'hi!') #send to yourself 
