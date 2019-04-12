# this is d11 excercise for 3rd-party library yagmail,requests,pyquery
# date : 2019.3.28
# author by : qiming

# update date : 2019.3.30
# content: add argument 'num' to funciton 'stats()' 
# update by : qiming

import requests
from pyquery import PyQuery
from mymodule import stats_word


# 定义stats函数，通过url获取文本并分析
def stats (url,num) :
    response = requests.get(url)
    # 提取微信公众号正文
    document = PyQuery (response.text)
    content = document ('#js_content').text() 
    # 统计前100词频
    statList = stats_word.stats_text(content,num)
#    statString = ''.join(str(i) for i in statList)
    statDict = dict(statList)
    return statDict

# 发送邮件功能的实现方法（暂不需要）
# import yagmail
# import getpass

# 设置发件人、登录密码、收件人
# sender = input('请输入发件人邮箱地址：')
# psw = input('请输入发件人邮箱登录密码：')
# recipient = input('请输入收件人邮箱地址：')
# smtp = 'smtp.163.com'

# 将统计结果发送到 pythoncamp@163.com，title: 19100101 qiming
# yagmail.SMTP(sender,psw,smtp).send(recipient,'19100101 qiming',statString)    
