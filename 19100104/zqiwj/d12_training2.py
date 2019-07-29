# 导入模块
from wxpy import *
from mymodule import stats_word
from pyquery import PyQuery
import requests

# 1、监听好友消息
# 2、如果朋友为分享类型的消息，则获取消息的网页链接(msg.url)
# 3、导入stats_word方法
# 4、分析msg.url词频
# 5、将词频结果返回给发送消息的好友

# 初始化机器人，扫码登陆
bot = Bot()

'''
my_friend = bot.friends().search('小兔子')[0]  # test
my_friend.send('d12测试作业')
'''

@bot.register()
def print_others(msg):
    print (msg.type)
    if msg.type =='Sharing':

        response = requests.get(msg.url)    # 请求获得内容
        
        document = PyQuery(response.text)    # 解析提出内容
        content = document('#js_content').text()
       
        result =stats_word.stats_text(content)
        content1 = result.most_common(100)
        day12 = str(content1)
        # print("111",day12)
        msg.reply(day12)

embed()    # 让程序保持运行
