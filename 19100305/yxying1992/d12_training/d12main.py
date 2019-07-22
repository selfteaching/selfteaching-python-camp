import requests
from pyquery import PyQuery
import stats_word
from wxpy import Bot,Message,embed # 导入模块

def main():
    bot = Bot() #登录微信的命令
    my_friend = bot.friends() #发给所有好友

    @bot.register(my_friend)

    def SHARING_Msg(msg):
        if msg.type == 'Sharing':
            response = requests.get(msg.url)
            document = PyQuery(response.text)
            contect = document('#js_content').text()
            c = str(stats_word.stats_text(content,10))
            msg.reply(c)
        else:
            print('waiting......')

    embed() #保持监听状态
    print(msg)

if __name__=='__main__':
    main()

