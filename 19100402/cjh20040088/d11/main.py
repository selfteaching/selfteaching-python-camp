from mymodule import stats_word
import requests
from pyquery import PyQuery

response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
print(response.text)

document=PyQuery(response.text)
content=document('#js_content').text()
print(content)

result=print(stats_word.stats_text_cn(content,100))



import getpass
sender=input('输入发件人邮箱：')
password=getpass.getpass('输入发件人邮箱密码：')
recipients=input('输入收件人邮箱：')

import yagmail
yag=yagmail.SMTP(sender,password,'smtp.qq.com')
subject='19100402 cjh20040088'
yag.send(to=recipients,subject=subject,contents=result)












    