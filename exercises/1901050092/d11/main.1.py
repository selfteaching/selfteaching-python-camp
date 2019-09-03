from mymodule import stats_word
from os import path
import requests
import pyquery
import yagmail
import getpass
import logging


logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|massage: %(massage)s',level=logging.DEBUG)

def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = pyquery.PyQuery(r.text)
    return document('#js.content').text()



def main():
    try:
        article = get_article()
        result = stats_word.stats_text_cn(article,10)
        logging.info('%s %s',type(result),str(result))
        sender = input('发件人邮箱：')
        password = getpass.getpass('发件人密码：')
        recipients = input('收件人邮箱：')
        yag = yagmail.SMTP(sender,password,'smtp.126.com')
        yag.send(recipients,'自学训练营7群 贾潇斌',str(result))
        logging.info('已发送')
    except Exception as e:
        logging.exception(e)


if __name__ == "__main__":
    main()