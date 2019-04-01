from wxpy import Bot,Message,embed
import d11_training1
#from pyquery import PyQuery
#from mymodule import stats_word
#初始化机器人，扫码登陆
bot = Bot()

@bot.register()
def print_others(msg):
    '''1、如果消息是Sharing类型，获取URL并对文本进行统计，输出前100的词频'''
    if msg.type == 'Sharing':#如果是sharing类型
        atou_url = msg.url
        result_url = d11_training1.auto_text(atou_url)
        msg.reply(result_url)#发送result的内容给好友

embed()     


    

