# this is d11 excercise for 3rd-party library yagmail,requests,pyquery
# date : 2019.3.28
# author by : qiming

import requests
import yagmail
import getpass
from pyquery import PyQuery
from mymodule import stats_word

# 设置发件人、登录密码、收件人
sender = input('请输入发件人邮箱地址：')
psw = input('请输入发件人邮箱登录密码：')
recipient = input('请输入收件人邮箱地址：')
smtp = 'smtp.163.com'

# 访问url获取微信公众号文章
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

# 提取微信公众号正文
document = PyQuery (response.text)
content = document ('#js_content').text() 

# 统计前100词频
statList = stats_word.stats_text(content,100)
statString = ''.join(str(i) for i in statList)

# 将统计结果发送到 pythoncamp@163.com，title: 19100101 qiming
yagmail.SMTP(sender,psw,smtp).send(recipient,'19100101 qiming',statString)    
