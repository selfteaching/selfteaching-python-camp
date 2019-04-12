from wxpy import Bot,Message,embed

def main():
    bot = Bot() #登录微信的命令
    my_friend = bot.friends() #发给所有好友

    @bot.register(my_friend)

    def SHARING_Msg(msg):
        if msg.type == 'Sharing':
            
            msg.reply(msg.url)
        else:
            print('waiting......')

    embed() #保持监听状态

if __name__=='__main__':
    main()