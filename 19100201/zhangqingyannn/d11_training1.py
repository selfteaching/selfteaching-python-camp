import requests
import yagmail
import getpass
from pyquery import PyQuery
from mymodule import stats_word

sender = input('请输入发件人邮箱地址:')
psw = input('请输入发件人邮箱登录密码:')
recipient = input('请输入收件人邮箱地址:')
smtp = 'smtp.qq.com'


response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

document = PyQuery (response.text)
content = document ('#js_content').text()

statList = stats_word.stats_text(content,100)
statString = ''.join(str(i) for i in statList)

yagmail.SMTP(sender,psw,smtp).send(recipient,'19100201,zhangqingyannn',statString)