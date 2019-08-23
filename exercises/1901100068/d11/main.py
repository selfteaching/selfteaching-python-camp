import yagmail
import requests
import pyquery
import getpass
import logging
from mymodule import stats_word

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message: %(message)s', level=logging.DEBUG)

def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()



def main():
    try:
        article = get_article()
        result = stats_word.stats_text_cn(article, 10)
        logging.info('%s %s', type(result), str(result))
        sender = input('发件人邮箱')
        password = getpass.getpass('发件人邮箱密码')
        recipients = input('收件人邮箱')
        yag = yagmail.SMTP(sender,password,'smtp.qq.com')
        yag.send(recipients,'1900100068-自学训练营学习15群 DAY11 chengfeng195', str(result))
        logging.info('已发送成功')
    except Exception as e:
        logging.exception(e)


if __name__=="__main__":
   main()



