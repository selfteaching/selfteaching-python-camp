from mymodule import state_word
import requests
import yagmail
import getpass
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA') 
 #从指定网站中请求信息

from pyquery import PyQuery
document = PyQuery(response.text) 
content = document('#js_content').text()
#提取微信公众号正⽂


sender = input("输入发件人邮箱：")
password = getpass.getpass("输入密码：")
recipients = input("输入收件人邮箱:")

result=state_word.stats_text_cn(content,100)
result1=str(result)
print(result1)
#调用state_word.py文件中的stats_text_cn函数实现：词频排序

yag = yagmail.SMTP(sender,password,host='smtp.qq.com')
yag.send('pythoncamp@163.com', '自学训练营10群，丸子', result1)
print('发送成功')
#发送邮件

