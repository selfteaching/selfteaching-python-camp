import requests
from pyquery import PyQuery
from mymodule import stats_word

def auto_text(url):
    '''1、使用requery获取url.
    2、导入stats_word模块，调用stats_text进行统计和词频处理，返回前100的结果'''
    r = requests.get(url)
    document = PyQuery(r.text)#提取公众号正文
    content = document('#js_content').text()
    return stats_word.stats_text(content,20)

#d12_training不要用到
#import getpass
#import yagmail
#设置发件人 登陆密码 收件人
#sender = input('输入发件人邮箱')
#password = getpass.getpass('输入发件人邮箱密码')
#recipients = input('输入收件人邮箱')
#smtp = 'smtp.qq.com'
#使用yagmail发送结果到pythoncamp@163.com
#yag = yagmail.SMTP(sender,password,smtp)
#yag.send(recipients,'19100101 xiaoguaishou01',result1)