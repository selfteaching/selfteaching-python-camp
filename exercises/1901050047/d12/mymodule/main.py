import requests  # 网络请求库
from pyquery import PyQuery  # 文档解析库
from stats_word import stats_text_cn  # 统计中文词频
from wxpy import *  # 导入微信机器人模块

bot = Bot(cache_path=True) # 初始化机器人，扫码登陆

my_friend = bot.friends() # 所有好友

@bot.register(my_friend,SHARING) # 消息接收监听器，获取分享类型的消息

def print_friend_messages(msg):
    response = requests.get(msg.url)    # 发送请求,url对应的页面内容
    document = PyQuery(response.text)     # 传入HTML代码
    content = document('#js_content').text()

    count = 100  # 统计100个中文词汇
    r_list = stats_text_cn(content,count)   # 统计前100个中文词频
    r_str = str(r_list)  # 转换成str类型

    msg.reply(r_str)  # 给好友回复消息
    #return r_str
 
embed() # 进入Python命令行，让程序保持运行

