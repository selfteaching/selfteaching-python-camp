import requests
from pyquery import PyQuery
import stats_word
import getpass

#用文章链接，获取返回结果
r = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")


#提取正文
d=PyQuery(r.text)
c=d('#js_content').text()

print(stats_word.stats_text_cn(c))

#发邮件
sender = input('13141360658@163.com')
passworld =getpass.getpass('piaolong123')
recipients = input('pythoncamp@163.com')



