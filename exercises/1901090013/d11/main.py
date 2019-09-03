from mymodule import stats_word
import logging
import yagmail
import requests
import getpass
import pyquery


logging.basicConfig(
    format='file:%(filename)s|line:%(lineno)d|message: %(message)s', level=logging.DEBUG)

def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()



def main():        #
    try:
        article = get_article()
        result = stats_word.stats_text_cn(article, 10)
        logging.info('%s %s', type(result), str(result))
        sender = input('请输入发件人邮箱：')#为保护密码输入的密码的时候不会显示出来，直接输入，完成后回车就行#
        password = getpass.getpass('输入发件人密码：')
        recipients = input('请输入收件人邮箱：')#如果是有的是qq/163邮箱 就填 smtp.qq.com/smtp.163.com
        yag = yagmail.SMTP(sender, password, 'smtp.qq.com')
        yag.send(recipients, '自学营008期01班 mynamezh', str(result))
        logging.info('已发送，请查收。')
    except Exception as e:
        logging.exception(e)        #捕获异常


if __name__ == "__main__":
    main()
