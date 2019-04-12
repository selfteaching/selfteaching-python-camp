#导入所需模块
import requests
from pyquery import PyQuery
from mymodule import stats_word
import yagmail
import getpass

#通过URL获取公众号文章
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

#获取公众号正文文本
document = PyQuery(response.text)
content = document('#js_content').text()

#对文本进行词频统计，输出前100的结果，并转换成字符串类型
statsList = stats_word.stats_text(content,100)
statsString = ''.join(str(i)for i in statsList)

#通过yagmail登录自己的邮箱，并将统计结果发送出去
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码：')
recipients = input('输入收件人邮箱：')
smpt = 'smpt.qq.com'
yagmail.SMTP(sender,password,smpt).send(recipients,'19100402 Autumn0808',statsString)