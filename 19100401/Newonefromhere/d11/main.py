
from mymodule import stats_word
import requests
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text()

output = stats_word.stats_text_cn(content,100)
output_str = str(output)
print(output_str,type(output_str))

import yagmail
import getpass
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')
host = 'smtp.163.com'
yag = yagmail.SMTP(sender,password,host)
subject = '19100401 Newonefromhere'
yag.send(to = recipients,subject = subject,contents = output_str)