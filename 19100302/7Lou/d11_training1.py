#步骤一：用requests代开链接
import requests
import pyquery
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
#步骤二：用pyquery解析网页
from pyquery import PyQuery
document = PyQuery(response.text) 
content = document('#js_content').text()
#步骤三：调用函数分频
from mymodule import stats_word
a=stats_word.stats_text(content)

#步骤四：将结果转为字符串 ？？？
b=''.join(str(i) for i in a)

#步骤五：通过yagmail把统计结果发邮件pythoncamp@163.com  参考他人代码，未发送成功？？？
import yagmail
import getpass

sender = input('输入发件人邮箱：')   
password = getpass.getpass('输入发件人邮箱密码：')
recipients = 'pythoncamp@163.com'
yag = yagmail.SMTP(sender, password, 'smtp.okstate.edu')
subject = '19100302 7Lou'
yag.send(to = recipients, subject = subject, contents = b)

print('发送邮件成功') 


