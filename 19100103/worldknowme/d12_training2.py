import re
import jieba
from collections import Counter
import requests
from wxpy import * 
bot=Bot(login_callback= True)

my_friend=bot.friends().search('阿肖')

@bot.register()              #打印来自好友的消息
def print_other(msg):
    print(msg)

@bot.register(my_friend)         #回复my_friend的消息
def reply_my_friend(msg):
    return 'received:{}({})'.format(msg.text,msg.type)

@bot.register(msg_types=SHARING)#监听好友分享的消息
def main():
    my_friend.send('兄弟，给我分享个公众号文章链接给我')
    response=requests.get('msg.url')
    from pyquery import PyQuery
    document=PyQuery(response.text)       #将内容抓取下来
    content=document('#js_content').text()      #获取正文内容
    import stats_word_d11
    s = stats_word_d11.stats_text(content,100)        #引用stats.text 来统计100个词
    s = str(s) 
    print(s)                                       #转为字符串str类型
    my_friend.send(s)
    embed()                                    #d堵塞线程，保持监听
if __name__=='__main__':
        main()
