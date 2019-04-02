# 导入模块
from wxpy import * 
import requests
from pyquery import PyQuery

# 初始化机器人，扫码登陆

bot = Bot()

# 搜索名称含有 "  " 的好友
#my_friend = bot.friends().search('杨文涛')[0]

    # 发送文本给好友
#my_friend.send('Hello WeChat!')

# 发送图片
#my_friend.send_image('my_picture.jpg')

#打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    if msg.type == SHARING :
        
        response = requests.get(msg.url) #提取公众号伪代码
        document = PyQuery(response.text)
        content = document('#js_content').text() #把抓取的内容写成可视的文字
        import mymodule.stats_word
        statlist = mymodule.stats_word.stats_text_cn(content,100)#统计内容的前100词频
        statString = "".join(str(i) for i in statlist)

        msg.reply_my_friend(statString)
# 进入 Python 命令行、让程序保持运行

embed()


#链接邮箱服务器
#sender = input('输入发件人地址:')
#password = getpass.getpass('输入发件人密码:')
#recipients = input('输入收件人地址:')
#smtp = 'smtp.126.com' #服务器地址
#Todo：在下面实现自己的分词统计和发送邮件的操作


# 回复 my_friend 的消息 (优先匹配后注册的函数!)
#@bot.register(my_friend)
#def reply_my_friend(msg):
   # return 'received: {} ({})'.format(msg.text, msg.type)

# 自动接受新的好友请求
#@bot.register(msg_types=FRIENDS)
#def auto_accept_friends(msg):

    # 接受好友请求
   # new_friend = msg.card.accept()

    # 向新的好友发送消息
    #new_friend.send('哈哈，我自动接受了你的好友请求')
    
    
# 进入 Python 命令行、让程序保持运行

#embed()

# 或者仅仅堵塞线程
# bot.join()