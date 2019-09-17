from mymodule import stats_word
import getpass
import yagmail
from wxpy import *

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message:%(message)s',level=logging.DEBUG)
def main():
    # 初始化机器人，扫码登录
    bot = Bot()
    # 找到好友和群聊
    my_friends = bot.friends()
    # family_group = bot.groups()

    # 监听好友信息，自动响应分享类型的消息
    @bot.register(my_friends,SHARING)
    def handler(msg):
        try:
            logging.info('sharing url=%s',msg.url)
            result = stats_word.stats_text_cn(stats_word.getcontent(msg.url),100)
            msg.reply(str(result))
        except Exception as e:
            logging.exception(e)
    embed()
if __name__ == '__main__':
    main()

