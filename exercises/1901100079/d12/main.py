from mymodule import stats_word
import logging
import pyquery
import requests
from wxpy import *

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG) 
# %(filename)s: 打印当前执行程序名；%(lineno)d: 打印日志的当前行号；%(message)s: 打印日志信息；level: 设置日志级别，debug是打印全部的日志,详细的信息,通常只出现在诊断问题上。

def get_artical(url):
    art=requests.get(url) 
    doc=pyquery.PyQuery(art.text)
    return doc('#js_content').text()

def main():
    bot=Bot()
    my_friend=bot.friends()
    @bot.register(my_friend,SHARING)
    def handler(msg):
        try:
            logging.info('分享的网址是：%s',msg.url)
            a=get_artical(msg.url)
            output=stats_word.stats_text_cn(a,100)
            msg.reply(str(output))    
        except Exception as i:
            logging.exception(i)
    embed()

if __name__=='__main__':
    main()         