from mymodule import stats_word
import requests
from pyquery import PyQuery
import getpass
import yagmail

url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
r = requests.get(url)
document = PyQuery(r.text)
content = document('#js_content').text()

content_list = stats_word.stats_text(content, 100)

content_list_str = [str(i) for i in content_list]
content_str = ''.join(content_list_str)

sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码：')
recipients = input('输入收件人邮箱：')

yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com')
contents = [content_str]
yag.send(recipients,'自学训练营学习20群 DAY11 GVguide', contents)
