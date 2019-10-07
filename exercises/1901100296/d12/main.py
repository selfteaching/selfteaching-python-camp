from mymodule import stats_word
import getpass
import yagmail
from wxpy import *
# import wxpy


def postemail(content,title):
    sender = input('输⼊发件⼈邮箱:')
    password = getpass.getpass('输⼊发件⼈邮箱密码(可复制粘贴):') 
    recipients = input('输⼊收件⼈邮箱:')
    yag = yagmail.SMTP(sender,password)
    yag.send(recipients,title,content)


# 初始化机器人，扫码登录
bot = Bot()
# 找到好友和群聊
my_friend = bot.friends().search('老运')[0]
# family_group = bot.groups().search('家人')[0]

# 发送消息给好友
my_friend.send('hello!')
# my_friend.send_image('1.jpg')
# 自动响应消息
# 打印消息
@bot.register()
def just_print(msg):
    print(msg)
# 取得消息内容的URL
@bot.register()
def get_url(msg):
    if msg.type == SHARING:
        content = stats_word.stats_text_cn(stats_word.getcontent(msg.url),100)
        # 回复好友消息
        @bot.register(my_friend)
        def reply_my_friend():
            return '处理结果：{}'.format(content)

embed()
# if __name__ == '__main__':
    # url='https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
    # content = stats_word.stats_text_cn(stats_word.getcontent(url),100)
    # print('统计结果：',content)
    # postemail(content,'统计结果')

