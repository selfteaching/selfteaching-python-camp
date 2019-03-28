import requests
import pyquery
import yagmail
import getpass
from pyquery import PyQuery
from mymodule import stats_word
#使用requery获取微信公众号文章
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(r.text)#提取公众号正文
content = document('#js_content').text()

#设置发件人 登陆密码 收件人
sender = input('输入发件人邮箱')
password = getpass.getpass('输入发件人邮箱密码')
recipients = input('输入收件人邮箱')
smtp = 'smtp.qq.com'

#导入stats_word模块，调用stats_text进行统计和词频处理，返回前100的结果
result = stats_word.stats_text(content,100)
result1 = str(result)
print(result1)

#使用yagmail发送结果到pythoncamp@163.com
yag = yagmail.SMTP(sender,password,smtp)
yag.send(recipients,'19100101 xiaoguaishou01',result1)