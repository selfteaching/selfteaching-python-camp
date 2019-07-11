


import yagmail
import requests
import pyquery
import getpass
import logging
from mymodule import stats_word

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message: %(message)s', level=logging.DEBUG)


# 提取微信公众号文章正文
def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()


def main():
    try:
        article = get_article()
        result = stats_word.stats_text_cn(article, 100)
        logging.info('%s %s', type(result), str(result))
        sender = input('请输入发件人邮箱:')
        password = getpass.getpass('请输入发件人邮箱密码:')
        recipients = input('请输入收件人邮箱:')
        yag = yagmail.SMTP(sender, password, 'smtp.163.com')
        yag.send(recipients, '自学训练营学习4群 wendy88888', str(result))
        logging.info("已发送，请注意查收")
    except Exception as e:
        logging.exception(e)
    
if __name__ == "__main__":
    main()






