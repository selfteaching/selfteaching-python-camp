import requests
import yagmail
import getpass
from pyquery import PyQuery
from mymodule import d11_stats_word

# 访问url获取微信公众号文章
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

# 提取微信公众号正文
document = PyQuery (response.text)
content = document ('#js_content').text() 

# 统计前100词频
statList = d11_stats_word.stats_text(content)
statString = ''.join(str(i) for i in statList)
print(statString)

sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')
smtp = 'smtp.qq.com'

yagmail.SMTP(sender,password,smtp).send(recipients,'19100105 liwanlsl',statString)
