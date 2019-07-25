import stats_word
import json
import requests
from pyquery import PyQuery 
import yagmail
import getpass

url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
response = requests.get(url)
print(response.text)


document = PyQuery(response.text)
content = document('#js_content').text()

r1= stats_word.stats_text_cn(content,100)
r2 = ''.join(str(i) for i in r1)

print (r2)

sender = input("请输入您的发件人邮箱:")
password =  getpass.getpass("输入发件人邮箱密码:")


yagmail.register(sender, password)
yag =yagmail.SMTP(sender,password,'smtp.qq.com')
yag.send('pythoncamp@163.com', '1901050028 boby2028', r2)
print("发送成功")
