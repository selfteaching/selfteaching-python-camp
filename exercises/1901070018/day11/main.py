from mymodule import stats_word
import os
import requests
from pyquery import PyQuery
import yagmail
import getpass

sender = input('输入发件人邮箱：')
passwd = getpass.getpass('输入发件人邮箱密码（可复制黏贴）：')
recipients = input('输入收件人邮箱：')



r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(r.text)
content = document('#js_content').text()
li1 = stats_word.stats_text_cn(content)
s = ''
li2 = []
for i in li1:
    li2.append('\'{}\'出现{}；'.format(i[0],i[1]))
li2.insert(0, '前{}个单词及其出现次数：'.format(len(li2)))
s1 = s.join(li2)

yag = yagmail.SMTP(user=sender,password=passwd, host='smtp.qq.com')
yag.send(recipients,'【1901070018】自学训练营18群 DAY11 yangbisheng', s1)






