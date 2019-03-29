import requests
import yagmail
import getpass
from pyquery import PyQuery 
from mymodule import stats_word

image_url = "https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"
response = requests.get(image_url)
document = PyQuery(response.text)
content = document('#js_content').text()
 
sender = input('输入发件人邮箱地址：')
password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')
recipient = input('输入收件人邮箱地址：')


yag = yagmail.SMTP(user=sender,password=password,host='smtp.qq.com')
content = [stats_word.stats_text_cn(content,100)]
yag.send(recipient,'lidong2119 d11',content)