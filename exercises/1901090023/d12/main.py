'''Day12任务：用wxpy库完成微信好友分享的网页链接，并解析该链接内容，将其中词频最高的前100个词的结果返回给好友'''

import requests
import pyquery      
from mymodule.stats_word import stats_text     # 从 模块中(mymodule是包，stats_word是模块) 导入 函数stats_text

# 第一步：引入wxpy模块，监听好友消息，获取SHARING类型消息的网页链接
import wxpy                                   # 导入wxpy模块
bot = wxpy.Bot()                              # 初始化机器人，会出现一个二维码，扫码登录即可
my_friend = bot.friends().search('熊小腰')[0]  # 搜索名字含有“熊小腰”的朋友(如果针对所有好友，则是my_friend=bot.friends())
@bot.register(my_friend, wxpy.SHARING)        # 接受好友类型为sharing的消息
def receive_mf(msg):                          # 参数msg为监听到的消息 
    r = requests.get(msg.url)                 # 请求sharing类型消息的网页链接
    
# 第二步：将获取的链接用Day11项目中的代码进行处理
    document = pyquery.PyQuery(r.text)            # 通过pyquery解析该网页
    content = document('#js_content').text()      # '#js_content'是网页的一个标签名，这个标签中存放着文档的内容。
    text=content                                  # 将content赋值给text
    dict_result = stats_text(text,100)            # 把结果赋值给dict_result

# 第三步：将处理结果返回给发送消息的好友
    msg.reply(str(dict_result))   #str()函数将某一类型的变量或者常量转换为字符串，回复好友
    # 法二是：my_friend.send(str(dict_result))
    # 法三是：return str(dict_result)
wxpy.embed()             # 进入Python命令行，让程序保持运行
