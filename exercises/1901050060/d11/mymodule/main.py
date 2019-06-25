import stats_word
import requests
from pyquery import PyQuery
import getpass
import yagmail

response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document=PyQuery(response.text)
content=document('#js_content').text()
result= stats_word.stast_text_cn(content,100)
result_str = ''.join(str(i) for i in result)
print('结果为：',result_str)

sender=input('输入发件人邮箱：')
password=getpass.getpass('输入发件人邮箱密码：')
recipients='pythoncamp@163.com'
files=result_str
yagmail.SMTP(sender,password).send(recipients,'自学训练营学习7群DAY11 ooocooc',result_str)
yag=yagmail.SMTP(sender,password,host='smtp.qq.com')
yag.send(recipients,'自学训练营学习7群DAY11 ooocooc',files)
