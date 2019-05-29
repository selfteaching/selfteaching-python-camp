import yagmail
import requests
import pyquery
from wxpy import *     #为什么不跟上面的一样
from mymodule import stats_word

#安装依赖包 wxpy
#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple wxpy

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)

#提取微信公众号文章正文
def get_article(url):
    r = requests.get(url)
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text() 

def main():
    bot = Bot()
#<<<<<<< master
    friends = bot.friends().search('青baby')
    #friends.send("hello")
#=======
    friends = bot.friends()

#>>>>>>> master
    @bot.register(friends,SHARING)
    def handler(msg):
        try:
           logging.info('sharing url = %s',msg.url)
           article = get_article(msg.url)  
           result = stats_word.stats_text_cn(article,100)     
#<<<<<<< master
           
           #msg.reply(str(result))
           #return 'received: {} ({})'.format(result)
            new_friend = msg.card.cccept()
            new_friend.send("str(result)")
        except Exception as e:
            logging.exception(e)
        embed()

if __name__ =="__main__":
    main()
    print()
#=======
           msg.reply(str(result))
        except Exception as e:
            logging.exception(e)
    embed()

if __name__ =="__main__":
    main()
#>>>>>>> master

    

