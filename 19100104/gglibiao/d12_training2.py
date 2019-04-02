
from wxpy import *                      #导入模块
bot = Bot(login_callback= True)                             #初始化机器人

bot.enable_puid('wxpy_puid.pkl')
my_friend = bot.friends().search('匆匆过客')[0]         #找到要聊天的好友
my_friend.send('send me some thing')                   #给好友发送一条消息
print(my_friend.puid)

@bot.register(my_friend,SHARING)                                #机器人初始化
def friend_sharing(msg):                                #定义这个分析分享内容的函数函数
                link = msg.url                        #获取该消息的地址
                import d11_training1                    #导入昨天的模块
                content=d11_training1.pro_art(link,20)  #这里对昨天的模块进行了分装，把发邮件之外的代码放到了一个函数里
                print(content)
                msg.reply(content)                 #给好友发送内容

# @bot.register(my_friend)
# def reply_msg(msg):
#         my_friend.send('这是自动回复')

# @bot.register()
# def print_msg(msg):
#         print(msg)

myself = bot.self
bot.file_helper.send('Hello from wxpy!')
       
embed()                         #保证程序运行