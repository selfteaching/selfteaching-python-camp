from mymodule import stats_word
import logging
import yagmail
import requests
import getpass
import pyquery
from pyquery import PyQuery
from wxpy import *


bot = Bot()

@bot.register(msg_types = SHARING)# 自动接受新的好友请求

def reply_my_friend(msg):
    r = requests.get(msg.url)#使⽤requests请求信息中的url
    document = pyquery.PyQuery(r.text)
    contents = document('#js_content').text()#将response.text用pyquery把链接中内容提取出来
    result = str(stats_word.stats_text_cn(contents,20))
    #使⽤用stats_word中的stats_text对提取结果进⾏行行分析和词频统计处理理(返回前20个词的 统计结果)
    msg.reply(result)#将处理结果返回给发送消息过来的好友

embed()


# logging.basicConfig(
#     format='file:%(filename)s|line:%(lineno)d|message: %(message)s', level=logging.DEBUG)

# def get_article():
#     r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
#     document = pyquery.PyQuery(r.text)
#     return document('#js_content').text()



# def main():        #
#     try:
#         article = get_article()
#         result = stats_word.stats_text_cn(article, 10)
#         logging.info('%s %s', type(result), str(result))
#         sender = input('请输入发件人邮箱：')#为保护密码输入的密码的时候不会显示出来，直接输入，完成后回车就行#
#         password = getpass.getpass('输入发件人密码：')
#         recipients = input('请输入收件人邮箱：')#如果是有的是qq/163邮箱 就填 smtp.qq.com/smtp.163.com
#         yag = yagmail.SMTP(sender, password, 'smtp.qq.com')
#         yag.send(recipients, '自学营008期01班 mynamezh', str(result))
#         logging.info('已发送，请查收。')
#     except Exception as e:
#         logging.exception(e)        #捕获异常


# if __name__ == "__main__":
#     main()


