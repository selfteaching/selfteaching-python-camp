# having something wrong with the word_stats.py which i can not figure it out yet. 
# following codes are made after read the READ.ME file of yagmail+request+other seftteaching-python-cap learners

import requests
from pyquery import PyQuery
import sys
sys.path.append("/Users/SeanChen/Documents/GitHub/selfteaching-python-camp/19100303/gogogomove/mymodule")
from stats_word import stats_text_cn

#请求微信公众号文章链接，获取返回结果（response）+ 将response.tex用pyquery把微信公众号正文提取出来
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()

#使用stats_word中的stats_text对提取结果进行分析和词频统计(返回前100个词的统计结果)，将结果转化为str类型
statlist=stats_text_cn(content,100)
statstring=''.join(str(i) for i in statlist)

# 通过yagmail登陆自己的邮箱，发送统计结果到pythoncamp@163.com
import yagmail
import getpass
sender = input('输入发件人邮箱：')   
password = getpass.getpass('输入发件人邮箱密码：')
recipients = input('输入收件人邮箱：')
yag = yagmail.SMTP(sender, password)
subject = '19100303 gogogomove'
yag.send(to = recipients, subject = subject, contents = statstring)

print('发送邮件成功') 