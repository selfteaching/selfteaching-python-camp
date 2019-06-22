import stats_word
import requests
import yagmail
from pyquery import PyQuery as pq
import getpass

#获取数据
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = pq(r.text)
content = document('#js_content').text()
#统计词频
result = stats_word.stats_text(content,0,100)
#发送邮件
sender = input('输⼊发件⼈邮箱:')
password = getpass.getpass('输⼊发件⼈邮箱密码(可复制粘贴):')
recipients = input('输⼊收件⼈邮箱:')
title = '自学训练营学习3群 DAY11 PowerZCY'
yagmail.SMTP(sender,password,'smtp.163.com').send(to = recipients,subject = title,contents = str(result))


