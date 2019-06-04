
from stats_word import stats_text

import json
import jieba
with open('I:/Github/selfteaching-python-camp/exercises/1901050045/d09/mymodule/tang300.json',encoding='UTF-8') as f:
    text=f.read()
f.closed
    
try:
    stats_text(text,10)
except ValueError:
    
    print ('参数格式错误或参数不存在,请重新输入字符串')
#DAY11作业在下面
import requests
response=requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text()
a= stats_text
a="".join(str(a(content,100)))
import getpass
sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码：')
recipients = 'pythoncamp@163.com'
import yagmail
#yag = yagmail.SMTP()
#contents = ['This is the body, and here is just text http://somedomain/image.png','You can find an audio file attached.', '/local/path/song.mp3']
#yag.send('to@someone.com', 'subject', contents)
#Or yagmail.SMTP('mygmailusername').send('to@someone.com', 'subject', 'This is the body')
#Note yag = yagmail.SMTP('mygmailusername', 'mygmailpassword')


yag = yagmail.SMTP(sender,password)
yag.send(recipients, '自学训练营学习4群DAY11董晓雄', a)


#不知道可不可以用这行命令代替getpass功能，yag = yagmail.SMTP(input('mygmailusername:'), input('mygmailpassword:'))