#from models.stats_word_12 import *
# import json

# with open('E:/python/day11/tang300.json', 'r', encoding='utf-8') as file:
#     str = file.read()
#     count=20
#     try:
#         print(f'输出词频最高的前20个汉字词频：{stats_text_cn(str,count)}')
#     except :
#         print('are you sure this is a string')


#day 11

# response=requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
# document = PyQuery(response.text)
# content = document('#js_content').text()
# #print(content)
# count=100
# a=str(stats_text(content,count))
# print(a)


# import getpass
# sender = input('输⼊入发件⼈人邮箱:')
# password = input('输入密码：')
# recipients = '535652072@qq.com'
# import yagmail
# yag=yagmail.SMTP(user=sender,password=password,host='smtp.126.com')

# contents=a
# subject='自学营008期01班 xujalg'
# yag.send(recipients,subject,contents)


#day12
from models.stats_word_12 import *
from wxpy import *
import requests  
from pyquery import PyQuery

bot = Bot(cache_path=True) #扫码登录
my_friend = bot.friends()  # 好友
@bot.register(my_friend,SHARING) #监听

def print_friend_messages(msg):
    response=requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    count= 20  
    my_list= stats_text_cn(content,count)   # 统计中文词频
    my_str = str(my_list)  # 转换成str类型
    msg.reply(my_str)  # 给好友回复消息
embed()

