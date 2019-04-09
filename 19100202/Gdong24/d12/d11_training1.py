#import package 
import requests
import yagmail
import getpass
import stats_word
from pyquery import PyQuery


#设置发件人、登录密码、收件人
sender = input('请输入发件人邮箱地址：')
psw = input('请输入发件人邮箱登录密码：')
recipient = input('请输入收件人邮箱地址：')
smtp = 'smtp.qq.com'

#获取微信公众号文章   
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

#提取微信公众号正文
document = PyQuery (response.text)
content = document ('#js_content').text() 
#print(content)

#pythoncamp@163.com

#Day8内容，尝试引用
try:
    print('前100的中文词频统计结果： ', stats_word.stats_text_cn(content))  #没有英文，直接调用的中文统计
except:
    print("对象不是字符串类型！")

# 统计前100词频
statList = stats_word.stats_text_cn(content)
statString = ''.join(str(i) for i in statList)
print(statString)

#将统计结果发送到 
#yagmail.SMTP(sender,psw,smtp).send(recipient,'19100202 gdong',statString)  

