from mymodule import stats_word
import requests
from pyquery import PyQuery
import getpass
import yagmail
import logging

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message: %(message)s', level=logging.DEBUG)

def getarticle():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = PyQuery(r.text)
    return document('#js_content').text()

def main():
    try:
        text = getarticle()
        mail_body = stats_word.stats_text_cn(text, 100)
        sender = input('输入发件人邮箱：')
        password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')
        recipients = input('输入收件人邮箱：')
        yag = yagmail.SMTP(sender, password, 'smtp.qq.com')
        yag.send(recipients, '【1901100065】自学训练营学习14群 Day11 dionysians', str(mail_body))
        logging.info('已发送，请注意查收。')
    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    main()
