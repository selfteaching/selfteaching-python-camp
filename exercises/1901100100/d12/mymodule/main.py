import requests
import logging
from pyquery import PyQuery as pq
import getpass
import stats_word
from wxpy import *

logging.basicConfig(filename='mylog.log',level=logging.DEBUG)
def stats_msg(url):
    r = requests.get(url)
    #get all the content of the web
    document = pq(r.text)
    content = document('#js_content').text()
    #get the useful text by the pyquery way
    dict1_order = stats_word.stats_text_cn(content,100)
    #get the order of the 100th number
    return str(dict1_order)
def main():
    bot = Bot()
    bot.file_helper.send('hello world!')        #test
    my_friend = bot.friends().search('以武入道')[0]
    my_friend.send('Hello WeChat!')

    @bot.register(chats=Friend)
    def friend_msg(msg):
        """接收好友消息"""
        try:
            print(msg)
            if msg.type == SHARING:
                print('接收到了链接')
                        
                my_friend.send(stats_msg(msg.url))  #reply my friend the stats result
            if msg.type  == TEXT:
                print(msg)
                my_friend.send(msg) 
            else:
                pass
        except Exception as e:
            logging.exception(e)    
    embed()

if __name__ == '__main__':
    main()

