import yagmail
import requests
from pyquery import PyQuery as py
import stats_word as sw
import getpass

r = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA") #获取网页的数据
web_text = r.text
document = py(web_text)
content = document('#js_content').text()
#print(content)

result = sw.stast_text_cn(content,100)
result = str(result)

sender = input("请输入发件人的邮箱：")
password = getpass.getpass("请输入发件人邮箱的密码：")

yagmail.register(sender,password)
yag = yagmail.SMTP(sender,password,'smtp.qq.com')
yag.send('pythoncamp@163.com','1901050059 jeasonlj525',result)
print("发送成功")

