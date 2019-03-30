# Date:19/03/28

import requests
# import yagmail
# import getpass
from pyquery import PyQuery
from mymodule import stats_word

# sender = input('请输入发件人邮箱地址:')
# psw = input('请输入发件人邮箱登录密码:')
# recipient = input('请输入收件人邮箱地址:')
# smtp = 'smtp.qq.com'

def stats (url,num):
    response = requests.get(url)
    document = PyQuery (response.text)
    content = document ('#js_content').text()

    statList = stats_word.stats_text(content,num)
    #statString = ''.join(str(i) for i in statList)
    statDict = dict(statList)
    return statDict

# yagmail.SMTP(sender,psw,smtp).send(recipient,'19100101 WangRui0802',statString)


