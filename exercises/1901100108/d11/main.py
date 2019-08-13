from mymodule import stats_word 
import logging
import yagmail
import requests
import pyquery
import getpass


logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|mesage: %(message)s', level=logging.DEBUG)

def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()

def main():
    try:
        article = get_article()
        result = stats_word.stats_text_cn(article,100)
        logging.info('%s %s', type(result), str(result))
        sender = input('请输入发件人邮箱：')
        password = getpass.getpass('请输入发件人邮箱密码：')
        recipients = input('请输入收件人邮箱：')
        yag = yagmail.SMTP(sender, password, 'SMTP.qq.com')
        yag.send(recipients, '【1901100108】⾃学训练营学习16群 DAY11 Mathophy', str(result))
        logging.info('已发送，请注意查收。')
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    main()