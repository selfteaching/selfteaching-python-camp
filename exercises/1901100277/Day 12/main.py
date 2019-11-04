#使用另一个个人微信分享一篇文章 给登录微信机器人的个人微信号,并统计好文章词频,将处理结果返回给发送消息过来的好友

# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()
# 找到所以好友 
my_friend = bot.friends()

# 监听好友信息，自动响应分享类型的消息
@bot.register(my_friend,SHARING)   #对于 --我的好友和其他群聊中 分享类型 SHARING的消息:
# @bot.register([my_friend,Group],SHARING)   #对于 --我的好友和其他群聊中 分享类型 SHARING的消息:
def get_friend_url(msg) :
    if isinstance(msg.type,SHARING):
        import requests
        response=requests.get(msg.url)

        from pyquery import PyQuery
        document=PyQuery(response.text)
        content=document('#js_content').text()

        from mymodule import stats_word  
        email_content = str(stats_word.stats_text_cn(content))

        msg.reply(email_content)

        # print ("我的好友或群里成员 分享的内容,转化为从大到小的词频为 >>>" + email_content)

# 进入 Python 命令行、让程序保持运行
embed()