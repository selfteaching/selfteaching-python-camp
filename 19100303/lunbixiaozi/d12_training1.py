from pyquery import PyQuery
from wxpy import *
import yagmail
import requests
import getpass
import mymodule.stats_word


#def main():
    # bot = Bot() #扫描二维码登录微信
    # my_friend = bot.friends() #回复对象为所有好友

    # @bot.register(None,None) #接受分享类消息
    # def auto_reply(msg):
    #     # response = requests.get(msg.url) #msg.url为分享的网址
    #     # document = PyQuery(response.text)
    #     # content = document('#js_content').text()
    #     #处理文本
    #     result = 'lala' #stats_word.stats_text_cn(content,100)
    #     return result #将结果返回给好友

    # embed() #堵塞线程，保持监听状态

# if __name__ == '__main__':
#     main() 

bot = Bot()
myself = bot.self
bot.file_helper.send('Hello from wxpy!')

@bot.register()
def print_messages(msg):
    if msg.type == SHARING:
        r=requests.get(msg.url,auth=('user','pass')) 
        document=PyQuery(r.text)
        content=document('#js_content').text()
        counter_cn_dict = mymodule.stats_word.stats_text_cn(content, 100)
        counter_cn_string = str(counter_cn_dict)
        msg.reply(counter_cn_string)

embed()
# Inscription = '''
# Best regards
# Zheng Zhang
# MBA, Class of 2019, Stephen M. Ross School of Business
# Tauber Institute for Global Operations
# University of Michigan

# '''

# r=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA',auth=('user','pass'))
# document=PyQuery(r.text)
# content=document('#js_content').text()

# counter_cn_dict = mymodule.stats_word.stats_text_cn(content, 100)
# counter_cn_string = str(counter_cn_dict)

# mail_body = 'Hi \nHere are the most common 100 words in the speech: \n' + counter_cn_string + '\n\n' + Inscription
# print (mail_body)

# sender = input('输入发件人邮箱: ')
# password = getpass.getpass('输入发件人邮箱密码: ')
# recipients = input('输入收件人邮箱: ')

# yag = yagmail.SMTP('zhz@umich.edu', password)
# yag.send(recipients, '19100303 lunbixiaozi', mail_body)
