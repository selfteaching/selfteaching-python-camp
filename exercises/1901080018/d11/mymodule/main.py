import requests
from pyquery import PyQuery
import stats_word
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()
list1 = stats_word.stats_text(content,100)
str1 = "".join([str(i) for i in list1])
import getpass
sender = input('请输入发件人邮箱：')
password = input('请输入发件人邮箱密码：')
recipients = input('请输入收件人邮箱地址：')
import yagmail
mail = yagmail.SMTP(user = sender,password = password,host = 'smtp.qq.com')
mail.send(to=recipients,subject='【1901080018】自学训练营学习6群 DAY11 a382064574',contents=str1)
print('发送成功')