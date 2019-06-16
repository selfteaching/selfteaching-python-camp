from mymodule import stats_word
from pyquery import PyQuery
from lxml import etree
import urllib
import requests
import yagmail
import getpass

from wxpy import *

# response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
# document = PyQuery(response.text)
# content = document('#js_content').text()
# print(stats_text_cn(content,100))


# to = 'pythoncamp@163.com'
# subject = '【自学营008期01班】自学训练营 DAY11 yuxudng2018'
# a = stats_text_cn(content,100)
# body=str(a)

# sender = input('输入发件人邮箱')
# password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')

# yag=yagmail.SMTP(user=sender, password=password, host='smtp.163.com')
# yag.send(to, subject,body)


bot = Bot()
# myself = bot.self
# bot.self.add()
# bot.self.accept()
# bot.self.send('hi there')

# 这一句代码可以去掉了，以后可以自己使用
# my_friend = bot.friends().search('18399', sex=MALE, city="上海")[0]
@bot.register(msg_types=SHARING)
def my_friend_sharing(msg):
    
    r = requests.get(msg.url)
    document=PyQuery(r.text)
    content = document('#js_content').text()
    result=str(stats_word.stats_text_cn(content,20))
    # b=str(a)
    # 是回复，而不是发送，使用reply这个方法
    # 下面还需要使用msg，上面不能重新赋值
    print(result)
    msg.reply(result)
    
embed()