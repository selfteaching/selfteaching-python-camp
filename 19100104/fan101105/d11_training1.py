
from mymodule import stats_word
import yagmail
import requests
from pyquery import PyQuery
import getpass
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()
top100=str((stats_word.stats_txt_cn(content)))
print(top100)
sender = input('请输入发件人信箱:')
password = getpass.getpass('请输入发件人信箱密码（可复制粘贴）:')
recipients = input('请输入收件人邮箱:')
#链接邮箱服务器
yag = yagmail.SMTP( user=sender, password=password, host='smtp.sohu.com')

# 邮箱正文
contents = top100

# 发送邮件
yag.send(recipients, '19100104 fan101105', contents)




