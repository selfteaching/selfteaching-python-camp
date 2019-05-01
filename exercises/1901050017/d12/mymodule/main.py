# 1901050017 day12 sarah
# 1.监听好友信息，如果信息为 分享(SHARING)类型的消息，则获取消息的网页链接(msg.url)
# 2.将获取的链接使用 实战项目1 的方式进行处理并将处理结果返回给发送消息过来的好友
# 3.启动微信机器，扫码登录
# 4.使用另一个微信进行测试，观察是否会接收到正确的结果



import requests
from pyquery import PyQuery
import stats_word
from wxpy import *

bot = Bot() #扫码登录微信
my_friend = bot.friends().search('nina')[0] #find a friend who be wanted to chat
my_friend.send('send me somthing,please')

#定义好友变量
@bot.register(my_friend,SHARING) #接受share类信息
def reply_my_friend(msg):
    response = requests.get(msg.url)   
    document = PyQuery(response.text)    
    content = document('#js_content').text()
    #URL信息提取
    reply = stats_word.stats_text(content,100)
    reply1 = ''.join(str(i) for i in reply)
    return reply1
    print(reply1)
embed() #保持监听状态



