 # 通过requests请求连接，并返回对应结果
import requests
response = requests.get('http://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
print(response)

# 通过Pyquery及返回的response提取内容
from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text()

# 通过stats_word的分词程序，提取词频为前100的分词,并转换为str格式
import stats_word as sw
list_a = sw.stats_text(content,100)
a = ''
for i in range(len(list_a)) :
    a = a + str(list_a[i][0]) + ' ' + str(list_a[i][1]) + ', '
print(a)

# 通过yagmail将内容发送给指定邮箱，并通过getpass保护密码
import getpass
import yagmail
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人密码：')
recipients = input('输入收件人邮箱：')
# yagmail.register(sender, password)
yagmail = yagmail.SMTP(sender, password, host='smtp.163.com')
yagmail.send(recipients,'19100205 lihaotian007', a)