import sys
import logging
import requests
import pyquery
from wxpy import *
from mymodule import stats_word

# 安装包 wxpy
# 在我的电脑上，在c:\user\administrator\
# 目录下直接输入：# pip install wxpy

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s', level=logging.DEBUG)

def get_article(url):   #定义提取函数
    r = requests.get(url)   #请求提取网页（微信公众号）
    document = pyquery.PyQuery(r.text)  #pyquery提取文章正文
    return document('#js_content').text()   #提取正文伪代码

def main():
    bot=Bot()   #初始化机器人，扫二维码登录
    friends=bot.friends()   #接收所有朋友发给我的信息

    @bot.register(friends,SHARING)  #视频说是装饰器？register函数，每当收到朋友信息，就会处理
    
    def handler(msg):
        try:    # try-except  做一个包围，捕获可能的异常和logging+exception捕获异常 
            logging.info('sharing url = %s', msg.url)   #此处表示打印分享的url
            article = get_article(msg.url)  #获取正文
            result = stats_word.stats_text_cn(article, 100) #分词
            msg.reply(str(result))  #用调用reply的方法，回复刚才分词统计的结果，结果转换为str类型 
        except Exception as e:
            logging.exception(e)
        embed() #调用embed的方法，让程序不直接退出，一直运行程序。而不会因为发生了一次就停止了程序


if __name__=="__main__":
    main()